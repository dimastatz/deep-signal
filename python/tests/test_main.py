""" streaming """
from deepsignal import app
from deepsignal.streaming import server


def test_main():
    """tests main function"""
    assert app.main() == 0
    assert server.transcribe() == 0
