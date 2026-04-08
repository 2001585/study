import threading
import time

sem = threading.Semaphore(2)

def worker(name):
    print(f"{name} 대기중")
    with sem:
        print(f"{name} 입장")
        time.sleep(2)
        print(f"{name} 퇴장")

threads = []
for name in ["A", "B", "C", "D"]:
    t=threading.Thread(target=worker, args=(name,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

