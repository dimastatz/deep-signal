import pyaudio
import whisper
import librosa
import numpy as np
from io import BytesIO
import wave
import multiprocessing as mp


def transcribe(con, model: whisper.Whisper) -> str:
    p = pyaudio.PyAudio()

    memory_file = BytesIO()
    wave_file = wave.open(memory_file, "w")
    wave_file.setnchannels(2)
    wave_file.setframerate(16000)
    print(p.get_sample_size(pyaudio.paInt16))
    wave_file.setsampwidth(p.get_sample_size(pyaudio.paInt16))

    while True:
        if con.poll(timeout=1):
            buffer = con.recv()
            wave_file.writeframes(buffer)
            print(f"---> recieved {memory_file.getbuffer().nbytes}")

            d, sr = librosa.load(BytesIO(memory_file.getbuffer()))
            text = model.transcribe(d)
            print(text)

        else:
            continue


def capture(con):
    chunk, rate, record_sec = 4096, 16000, 5
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
        data = stream.read(chunk, exception_on_overflow=False)
        con.send(data)

    stream.close()
    p.terminate()
    print(f"* done recording")


if __name__ == "__main__":
    con1, con2 = mp.Pipe()
    model = whisper.load_model("base")

    proc = mp.Process(
        target=transcribe,
        args=(
            con2,
            model,
        ),
    )
    proc.start()
    capture(con1)
    proc.terminate()

    print("done")
