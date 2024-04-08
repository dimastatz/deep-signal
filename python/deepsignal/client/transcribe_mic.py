import time
import pyaudio
import multiprocessing as mp


def transcribe(con) -> str:
    data = con.recv()
    print("transcribe " + data)


def capture(con):
    chunk, rate, record_sec = 1024, 16000, 5
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=rate, input=True, frames_per_buffer=chunk)
    print("* recording")
    for _ in range(0, int(rate / chunk * record_sec)):
        data = stream.read(chunk)
        con.send(data)
    
    stream.close()
    p.terminate()
    print(f"* done recording")


if __name__ == "__main__" :
    con1, con2 = mp.Pipe()

    proc = mp.Process(target=transcribe, args=(con2,))
    proc.start()
    capture(con1)
    proc.terminate()

    print("done")