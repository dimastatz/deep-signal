""" integration of whisper """
import typing as tp

import whisper
import numpy as np


def get_transcriber() -> tp.Callable[[np.ndarray], str]:
    """create whisper transcriber"""
    model = whisper.load_model("base")

    def transcribe(buffer: np.ndarray) -> str:
        """run transcription"""
        return model.transcribe(buffer)

    return transcribe
