""" streaming """
import pytest
from deepsignal import app
from deepsignal.streaming import server


@pytest.fixture(scope="module", name="test_client")
def fixture_test_client():
    """tests main function"""
    with app.app.test_client() as client:
        with app.app.app_context():
            yield client


@pytest.fixture(scope="module", name="socketio_client")
def fixture_socketio_client(test_client):
    """test setup"""
    return test_client.test_client(app.app)


def test_client_connect(socketio_client):
    """tests connect"""
    assert socketio_client.is_connected()


def test_main(socketio_client):
    """tests main function"""
    assert server.transcribe() == 0
    socketio_client.emit("message", "Test message")
    assert "Test message" == socketio_client.get_received()[0]["args"][0]
