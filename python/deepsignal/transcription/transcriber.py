""" Implements Transcriber Worker for RT cases"""
import time
from queue import Queue
from typing import Callable
from threading import Thread
from whisper import Whisper


class Transcriber:
    """Implements Transcriber Worker for RT cases"""

    def __init__(
        self, model: Whisper, callback: Callable[[str, bool], None], max_size=1000
    ) -> None:
        """ctor"""
        self.model = model
        self.queue = Queue[bytes](max_size)
        self.worker = Thread(target=self._transcribe_loop)
        self.window = []
        self.result: str = None
        self.callback = callback

        # start worker
        self.worker.start()
        self.started = True

    def add_chunk(self, chunk: bytes) -> None:
        """add new audio chunk"""
        self.queue.put(chunk)

    def stop(self) -> None:
        """stop transcription loop"""
        self.started = False

    def _transcribe_loop(self):
        """background transcription job"""
        while self.started:
            while self.queue.not_empty:
                self.window.append(self.queue.get_nowait())

            if not self.window:
                time.sleep(0.1)
            else:
                buffer = self.to_numpy(self.window)
                result = self.model.transcribe(buffer, language="en")
                segment_closed = result == self.result
                self.callback(result, segment_closed)
