import threading
import time

lock=threading.Lock()

def worker(name):
    print(f"{name} : lock 대기중")
    with lock:
        print(f"{name} : lock 획득")
        time.sleep(1)
        print(f"{name} : 작업 끝")
    print(f"{name} : lock 반납")

t1=threading.Thread(target=worker, args=("A",))
t2=threading.Thread(target=worker, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()