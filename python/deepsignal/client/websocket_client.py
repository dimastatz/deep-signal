import wave
import pyaudio
import asyncio
import websockets


async def start_transcription():
    server = "einstein-transcribe.sfproxy.einsteintest1.test1-uswest2.aws.sfdc.cl"
    url = f"wss://{server}/transcribe/v1/tenant/stream?engine=aws"
    async with websockets.connect(url) as websocket:
        await asyncio.gather(capture_audio(websocket), receive_transcription(websocket))


async def capture_audio(websocket: websockets.WebSocketClientProtocol):
    chunk, rate, record_sec = 1024, 16000, 5
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=rate,
        input=True,
        frames_per_buffer=chunk,
    )
    print("* recording")
    for _ in range(0, int(rate / chunk * record_sec)):
        data = stream.read(chunk)
        await websocket.send(data)

    stream.close()
    p.terminate()
    print(f"* done recording")


async def receive_transcription(websocket):
    while True:
        text_data = await websocket.recv()
        print(text_data)


asyncio.run(start_transcription())
