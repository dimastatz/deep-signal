""" Implements Transcriber Worker for RT cases"""
import time
import json
from multiprocessing import Pipe, Process
from multiprocessing.connection import Connection

import whisper
import numpy as np


def transcribe(model: whisper.Whisper, chunks: list) -> dict:
    """transcribes given byte array"""
    buffer = b"".join(chunks)
    arr = np.frombuffer(buffer, np.int16).flatten().astype(np.float32) / 32768.0
    return model.transcribe(arr)


def transcribe_worker(conn: Connection, model: whisper.Whisper):
    """stream processing implementation"""
    chunks = []
    print(model.num_languages)

    while True:
        if conn.poll():
            chunk = conn.recv()
            if chunk == b"":
                if len(chunks) > 0:
                    result = transcribe(model, chunks)
                conn.send("finsihed")
                break

            chunks.append(chunk)
        else:
            if len(chunks) > 0:
                conn.send(str(len(chunks)))
                chunks.clear()
            else:
                time.sleep(0.1)


class Transcriber:
    """Stream State Manager"""

    def __init__(self, model_name="base") -> None:
        self.conn = Pipe()
        self.model = whisper.load_model(model_name)
        self.worker = Process(
            target=transcribe_worker,
            args=(
                self.conn[1],
                self.model,
            ),
        )

    def send(self, chunk: bytes) -> None:
        """Send audio chunk"""
        self.conn[0].send(chunk)

    def start(self) -> None:
        """Start streaming worker"""
        if not self.worker.is_alive():
            self.worker.start()

    def stop(self, timeout=3) -> None:
        """Stop streaming worker"""
        if self.worker.is_alive():
            self.send(b"")
        self.worker.join(timeout)

    def get_result(self) -> str:
        """Read all results produced"""
        result = []
        while self.conn[0].poll():
            result.append(self.conn[0].recv())
        return "\n".join(result)
