import threading

counter=0

def worker():
    global counter
    counter += 1
    print("worker에서 counter:", counter)

print("시작 counter:", counter)

t = threading.Thread(target=worker)
t.start()
t.join()

print("최종 counter:" , counter)
