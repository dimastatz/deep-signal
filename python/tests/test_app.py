""" streaming """
import logging as log

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


def test_index(test_flask_client):
    """test index page"""
    res = test_flask_client.get("/")
    assert res.status_code == 200

    text = str(res.get_data(), encoding="utf-8")
    log.info("server index %s", text)
    assert text == "WS Server"
