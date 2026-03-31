import os
from multiprocessing import Process

counter = 0


def worker():
    global counter
    counter += 1
    print("worker pid:", os.getpid())
    print("worker counter:", counter)


if __name__ == "__main__":
    print("main pid:", os.getpid())
    print("before counter:", counter)
    p = Process(target=worker)
    p.start()
    p.join()
    print("after counter:", counter)
