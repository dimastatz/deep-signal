""" test transcriptions """
import os
import io
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

    with open(path, "rb") as wav:
        content = wav.read()
        rate, buffer = wv.read(io.BytesIO(content))

        text = transcriber(buffer)
        print(text)
        
        assert rate > 0
