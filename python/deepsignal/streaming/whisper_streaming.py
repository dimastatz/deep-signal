""" implement whisper streaming """
import websockets
import deepsignal.transcription.whisper_wrapper as wp


async def websocket_handler(websocket):
    """websocket handler"""
    transcriber = wp.get_transcriber()

    try:
        # Start an infinite loop to handle incoming messages
        async for message in websocket:
            # Print the received message
            res = transcriber(message)
            # Echo the message back to the client
            await websocket.send(res)
    except websockets.exceptions.ConnectionClosedError:
        # Display a message when the client disconnects
        print("Client disconnected")
