from multiprocessing import current_process
import os
import threading
import time

def worker():
    print("worker 시작")
    print("worker 프로세스 ID:", os.getpid())
    print("worker 스레드 이름:", threading.current_thread().name)
    time.sleep(1)
    print("worker 종료")

print("메인 프로세스 ID:", os.getpid())
print("메인 스레드 이름:", threading.current_thread().name)

t=threading.Thread(target=worker, name="WorkerThread")
t.start()
t.join()

print("메인 종료")
