import threading
import time

lock_a=threading.Lock()
lock_b=threading.Lock()

def worker1():
    with lock_a:
        print("worker1: lock_a 획득")
        time.sleep(1)
        print("worker1: lock_b 대기")
        with lock_b:
            print("worker1: lock_b 획득")

def worker2():
    with lock_b:
        print("worker2: lock_b 획득")
        time.sleep(1)
        print("worker2: lock_a 대기")
        with lock_a:
            print("worker2: lock_a 획득")

t1=threading.Thread(target=worker1)
t2=threading.Thread(target=worker2)

t1.start()
t2.start()

t1.join()
t2.join()

print("종료")