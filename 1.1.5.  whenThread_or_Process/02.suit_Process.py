import os
import time
from multiprocessing import Process


def heavy_task():
    print("무거운 작업 프로세스 pid:", os.getpid())
    time.sleep(2)
    print("무거운 작업 종료")


if __name__ == "__main__":
    print("메인 pid:", os.getpid())
    p = Process(target=heavy_task)
    p.start()
    p.join()
    print("메인 종료")
