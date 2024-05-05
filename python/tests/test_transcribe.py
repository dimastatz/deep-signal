""" test transcriptions """
import os
import time
import difflib as df
import whisper
import librosa as lr
import deepsignal.transcription.transcriber as ts
import deepsignal.transcription.whisper_wrapper as ww


def test_whisper_transcribe():
    """test whisper transcribe"""
    expected = (
        " or was of heaven mine. Thus was then she."
        + " What as-be said Sarah, as to Lady for better, very stob."
    )

    transcriber = ww.get_transcriber()
    assert not transcriber is None

    path = os.getcwd() + "/tests/resources/sample-4.mp3"
    buffer, _ = lr.load(path)
    result = transcriber(buffer)
    print(result["text"], expected)

    assert df.SequenceMatcher(None, expected, result["text"]).ratio() > 0.9


def test_whisper_transcribe_stream():
    """test whisper in memory processing for streaming"""
    path = os.getcwd() + "/tests/resources/harvard.wav"

    transcriber = ww.get_transcriber()
    buffer, rate = lr.load(path)
    assert rate > 0
    text = transcriber(buffer)
    assert len(text) > 0

    def result_ready(text: str, is_partial: bool):
        print(text, is_partial)

    model = whisper.load_model("base")
    transcriber = ts.Transcriber(model, result_ready)
    while buffer.any():
        chunk = buffer[:4096]
        buffer = buffer[4096:]
        transcriber.add_chunk(chunk)
        time.sleep(0.1)

    transcriber.stop()
