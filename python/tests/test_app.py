""" streaming """
import os
import numpy
import pytest
import librosa
from deepsignal import app as flask_app


@pytest.fixture(name="test_flask_app")
def app():
    """return flask app"""
    yield flask_app.app


@pytest.fixture(name="test_flask_client")
def client(test_flask_app):
    """return flask client for tests"""
    return test_flask_app.test_client()


@pytest.fixture(name="test_socketio")
def socketio(test_flask_app, test_flask_client):
    """return flask app"""
    yield flask_app.socketio.test_client(
        test_flask_app, flask_test_client=test_flask_client
    )


def test_index(test_flask_client, test_socketio):
    """test index page"""
    res = test_flask_client.get("/")
    assert res.status_code == 200
    assert res.get_data() == b"WS Server"
    assert test_socketio.is_connected()

    test_socketio.send("test message 1")
    result = test_socketio.get_received()
    assert result[0]["args"][0]["data"] == "connected"
    assert result[1]["args"][0]["data"] == "test message 1"

    test_socketio.send("test message 2")
    result = test_socketio.get_received()
    assert result[0]["args"][0]["data"] == "test message 2"


def test_audio_stream(test_socketio):
    """test audio stream"""
    result = test_socketio.get_received()
    assert len(result) == 1

    path = os.getcwd() + "/tests/resources/sample-4.mp3"
    buffer, sample_rate = librosa.load(path)
    duration = int(librosa.get_duration(y=buffer, sr=sample_rate))
    assert len(buffer) > 0 and duration > 0

    length = int(len(buffer) / duration)

    while len(buffer) > 0:
        chunk = buffer[0: length]
        chunk_in = numpy.array2string(chunk)

        buffer = buffer[length:]
        test_socketio.send(chunk_in)
        result = test_socketio.get_received()
    
        chunk_out = result[0]["args"][0]["data"]
        assert chunk_out == chunk_in

