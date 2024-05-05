""" test transcriptions """
import os
import time
from multiprocessing import Pipe

import difflib as df
import librosa as lr
import whisper
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

    model = whisper.load_model("base")
    con_parent, con_child = Pipe()

    chunk = b"\x00\x00\x00\x00\x00"
    con_parent.send(chunk)
    con_parent.send(b"")
    ts.transcribe_worker(con_child, model)
    chunk_out = con_parent.recv()
    assert chunk_out == str(len(chunk))

    # add chunks in a player mode
    transcriber = ts.Transcriber()
    assert not transcriber.worker.is_alive()
    transcriber.start()
    assert transcriber.worker.is_alive()
    transcriber.send(b"\x00\x00\x00\x00\x00")

    time.sleep(1)
    result = transcriber.get_result()
    assert transcriber.worker.is_alive() and len(result) > 0

    transcriber.stop()
    assert not transcriber.worker.is_alive()
