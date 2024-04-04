""" test transcriptions """
import os
import time
import logging
import difflib as df
import librosa as lr
import scipy.io.wavfile as wv
import deepsignal.transcription.whisper_wrapper as whisper


def test_whisper_transcribe():
    """test whisper transcribe"""
    expected = (
        " or was of heaven mine. Thus was then she."
        + " What as-be said Sarah, as to Lady for better, very stob."
    )

    transcriber = whisper.get_transcriber()
    assert not transcriber is None

    path = os.getcwd() + "/tests/resources/sample-4.mp3"
    buffer, _ = lr.load(path)
    result = transcriber(buffer)
    print(result["text"], expected)

    assert df.SequenceMatcher(None, expected, result["text"]).ratio() > 0.9


def test_whisper_transcribe_chunks():
    """test whisper in memory processing for streaming"""
    path = os.getcwd() + "/tests/resources/harvard.wav"

    transcriber = whisper.get_transcriber()
    buffer, rate = lr.load(path)
    assert rate > 0

    while len(buffer) > 0:
        chunk = buffer[0:4096]
        buffer = buffer[4096:]
        start = time.time()
        result = transcriber(chunk)
        logging.info("time: %s, result: %s", time.time() - start, result)

