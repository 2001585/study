from multiprocessing import Process, ProcessError
import os

x=10

def worker():
    global x
    x=99
    print("worker pid: ",os.getpid)
    print("worker x:",x)

if __name__ == "__main__":
    print("main pid:",os.getpid)
    print("before x:", x)

    p=Process(target=worker)
    p.start()
    p.join()

    print("after x:", x)