""" Implements Transcriber Worker for RT cases"""
import time
from queue import Queue
from typing import Callable
from threading import Thread

import numpy as np
from whisper import Whisper


class Transcriber:
    """Implements Transcriber Worker for RT cases"""

    def __init__(
        self, model: Whisper, result_ready: Callable[[str, bool], None], max_size=1000
    ) -> None:
        """ctor"""
        self.model = model
        self.queue = Queue[bytes](max_size)
        self.worker = Thread(target=self._transcribe_loop)
        self.window = []
        self.result: str = None
        self.result_ready = result_ready
        # start worker
        self.started = True
        self.worker.start()

    def add_chunk(self, chunk: bytes) -> None:
        """add new audio chunk"""
        self.queue.put(chunk)

    def stop(self) -> None:
        """stop transcription loop"""
        self.started = False
        self.worker.join(3)

    def _transcribe_loop(self):
        """background transcription job"""
        while self.started:
            while not self.queue.empty():
                self.window.append(self.queue.get_nowait())

            if not self.window:
                time.sleep(0.1)
            else:
                buffer = b"".join(self.window)
                arr = (
                    np.frombuffer(buffer, np.int16).flatten().astype(np.float32)
                    / 32768.0
                )
                result = self.model.transcribe(arr, language="en")
                segment_closed = result == self.result
                self.result_ready(result, segment_closed)
                if segment_closed:
                    self.window.clear()
