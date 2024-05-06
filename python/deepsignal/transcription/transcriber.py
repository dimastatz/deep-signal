"""Implemet Transcriber worker"""
import time
from multiprocessing import Queue
from multiprocessing import Process

import whisper
import numpy as np


def transcribe(model: whisper.Whisper, chunks: list) -> dict:
    """transcribes given byte array"""
    buffer = b"".join(chunks)
    arr = np.frombuffer(buffer, np.int16).flatten().astype(np.float32) / 32768.0
    return model.transcribe(arr)


def transcribe_worker(queue_in: Queue, queue_out: Queue, model: whisper.Whisper):
    """stream processing implementation"""
    chunks, prev_res, times = [], None, 0

    def time_ms():
        return time.time() * 1000

    start = time_ms()

    while True:
        if not queue_in.empty():
            chunk = queue_in.get()

            # should stop transcription
            if chunk == b"":
                if len(chunks) > 0:
                    result = transcribe(model, chunks)
                    queue_out.put(
                        {"result": result, "is_partial": False, "time": time_ms() - start}
                    )
                queue_out.put(
                    {"result": "etp session ended", "is_partial": False, "time": time_ms() - start}
                )
                break

            # append chunks
            chunks.append(chunk)
        else:

            if len(chunks) > 0:
                result = transcribe(model, chunks)
                if prev_res == result["text"]:
                    times += 1
                else:
                    times = 0

                close_segment = times > 2 and result != ""

                queue_out.put(
                    {"result": result, "is_partial": not close_segment, "time": time_ms() - start}
                )

                if close_segment:
                    chunks.clear()
                    prev_res = None
                    times = 0
                else:
                    prev_res = result["text"]

            else:
                time.sleep(1)


class Transcriber:
    """Stream State Manager"""

    def __init__(self, model: whisper.Whisper) -> None:
        self.queue_in = Queue()
        self.queue_out = Queue()
        self.model = model
        self.worker = Process(
            target=transcribe_worker,
            args=(
                self.queue_in,
                self.queue_out,
                self.model,
            ),
        )

    def send(self, chunk: bytes) -> None:
        """Send audio chunk"""
        self.queue_in.put(chunk)

    def start(self) -> None:
        """Start streaming worker"""
        if not self.worker.is_alive():
            self.worker.start()

    def stop(self, timeout=3) -> None:
        """Stop streaming worker"""
        if self.worker.is_alive():
            self.send(b"")
        self.worker.join(timeout)

    def get_result(self) -> list:
        """Read all results produced"""
        result = []
        while not self.queue_out.empty():
            result.append(self.queue_out.get())
        return result