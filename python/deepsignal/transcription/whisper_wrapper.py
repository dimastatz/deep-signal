""" integration of whisper """
import whisper
import numpy as np


def get_transcriber():
    """create whisper transcriber"""
    model = whisper.load_model("base")

    def transcribe(buffer: np.ndarray) -> str:
        """run transcription"""
        return model.transcribe()
