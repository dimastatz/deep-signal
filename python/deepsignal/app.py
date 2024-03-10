""" main entry point """
from flask import Flask
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app)


# Define a route to serve the HTML file
@app.route("/")
def index():
    """default web page"""
    app.logger.info("index")
    return "WS Server"


@socketio.on("connect")
def handle_connect():
    """handle connect"""
    app.logger.info("connected")
    socketio.send("connected")


# Define the WebSocket event handler
@socketio.on("message")
def handle_message(message):
    """handle message"""
    app.logger.info("echo")
    socketio.send(message)


if __name__ == "__main__":  # pragma: no cover
    # Start the Flask application with Socket.IO support
    socketio.run(app, debug=True)
