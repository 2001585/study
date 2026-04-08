import threading
import time

counter=0

def worker():
    global counter
    for _ in range(1000):
        temp=counter
        time.sleep(0.0001)
        temp=temp+1
        counter = temp

t1=threading.Thread(target=worker)
t2=threading.Thread(target=worker)

t1.start()
t2.start()

t1.join()
t2.join()

print("기대값: ", 2000)
print("실제값: ", counter)
