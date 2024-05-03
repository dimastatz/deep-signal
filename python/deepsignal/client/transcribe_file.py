import time
import wave
import whisper
from pathlib import Path
from multiprocessing import Pipe, Process
from multiprocessing.connection import Connection


def run_server(con: Connection, model: whisper.Whisper):
    frames = []
    while True:
        if con.poll():
            frames.append(con.recv())
        else:
            time.sleep(0.1)
            print(f"{time.time()}: Frames {len(frames)}")


def run_client(con: Connection, fname: str):
    with wave.open(fname, 'r') as wavfile:
        params = wavfile.getparams()
        print(f"WavFile {params.sampwidth}, {params.nchannels}, {params.framerate}")


if __name__ == "__main__":
    con1, con2 = Pipe()
    model = whisper.load_model("base")
    path = str(Path(__file__).resolve().parent) + "/audio/harvard.wav"

    proc = Process(
        target=run_server,
        args=(
            con2,
            model,
        ),
    )

    proc.start()
    run_client(con1, path)
    time.sleep(1)
    proc.terminate()
