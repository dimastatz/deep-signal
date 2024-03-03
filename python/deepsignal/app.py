""" main entry point """
from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app)


# Define a route to serve the HTML file
@app.route("/")
def index():
    """default web page"""
    return render_template("index.html")


@socketio.on("connect")
def handle_connect():
    """handle connect"""
    print("Client connected")


# Define the WebSocket event handler
@socketio.on("message")
def handle_message(message):
    """handle message"""
    # Echo the message back to all connected clients
    socketio.send(message)


if __name__ == "__main__":
    # Start the Flask application with Socket.IO support
    socketio.run(app, debug=True)
