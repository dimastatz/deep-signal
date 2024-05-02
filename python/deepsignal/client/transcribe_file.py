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
    print(f"{time.time()}: Client")
    pass


if __name__ == "__main__":
    con1, con2 = Pipe()
    model = whisper.load_model("base")
    path = Path(__file__).parent.absolute()
    
    print(path)


    proc = Process(
        target=run_server,
        args=(
            con2,
            model,
        ),
    )

    proc.start()
    run_client(con1, "")
    time.sleep(1)
    proc.terminate()
