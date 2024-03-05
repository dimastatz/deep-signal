""" streaming """
import pytest
from deepsignal import app, socketio
from deepsignal.streaming import server


@pytest.fixture(scope="module")
def test_client():
    """tests main function"""
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture(scope="module")
def socketio_client(test_client):
    """test setup"""
    return socketio.test_client(app)


def test_client_connect(socketio_client):
    """tests connect"""
    assert socketio_client.is_connected()


def test_main():
    """tests main function"""
    assert server.transcribe() == 0

    socketio_client.emit("message", "Test message")
    assert "Test message" == socketio_client.get_received()[0]["args"][0]
