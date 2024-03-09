""" streaming """
import pytest
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

    test_socketio.send("test message")
    assert test_socketio.get_received()
