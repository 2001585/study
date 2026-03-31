import os
from multiprocessing import Process

data = [1, 2]


def worker():
    data.append(3)
    print("worker pid:", os.getpid())
    print("worker data:", data)


if __name__ == "__main__":
    print("main pid:", os.getpid())
    print("before data:", data)
    p = Process(target=worker)
    p.start()
    p.join()
    print("after data:", data)
