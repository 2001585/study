import threading
import time

counter = 0
lock = threading.Lock()


def worker():
    global counter
    for _ in range(1000):
        with lock:
            temp = counter
            time.sleep(0.0001)
            temp = temp + 1
            counter = temp


t1 = threading.Thread(target=worker, name="T1")
t2 = threading.Thread(target=worker, name="T2")

t1.start()
t2.start()

t1.join()
t2.join()

print("기대값: 2000")
print("실제값:", counter)
