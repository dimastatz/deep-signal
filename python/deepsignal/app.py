""" main entry point """
import numpy as np
from flask import Flask
from flask_socketio import SocketIO
from deepsignal.transcription.whisper_wrapper import get_transcriber


app = Flask(__name__)
socketio = SocketIO(app)
transcriber = get_transcriber()


@app.route("/")
def index():
    """default web page"""
    app.logger.info("index")
    return "WS Server"


@socketio.on("connect")
def handle_connect():
    """handle connect"""
    app.logger.info("connected")
    socketio.emit("response", {"data": "connected"})


# Define the WebSocket event handler
@socketio.on("message")
def handle_message(message):
    """handle message"""
    app.logger.info("echo")

    if isinstance(message, str):
        text = message
    else:
        buffer = np.frombuffer(message)
        text = transcriber(buffer)

    socketio.emit("response", {"data": text})


if __name__ == "__main__":  # pragma: no cover
    # Start the Flask with Socket.IO
    socketio.run(app, debug=True)
