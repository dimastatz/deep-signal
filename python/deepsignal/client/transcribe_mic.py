import time
import multiprocessing as mp


def transcribe(con) -> str:
    data = con.recv()
    print("transcribe " + data)


def capture(con):
    print("capture")
    con1.send("packet")
    time.sleep(1)


if __name__ == "__main__" :
    con1, con2 = mp.Pipe()

    proc = mp.Process(target=transcribe, args=(con2,))
    proc.start()
    capture(con1)
    proc.terminate()
    
    print("done")