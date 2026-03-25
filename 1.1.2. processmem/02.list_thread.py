import threading

items = []

def worker():
    items.append("apple")
    print("worker inside:", items)

print("before:", items)

t=threading.Thread(target=worker)
t.start()
t.join()

print("after:", items)

