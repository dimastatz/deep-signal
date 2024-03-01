""" test transcriptions """
import deepsignal.transcription.whisper_wrapper as whisper


def test_whisper_transcribe():
    """test whisper transcribe"""
    transcriber = whisper.get_transcriber()
    assert not transcriber is None
