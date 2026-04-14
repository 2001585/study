import threading

global_value = 0


def worker(name):
    global global_value
    local_value = 0

    global_value += 1
    local_value += 1

    print(f"{name} -> global_value: {global_value}, local_value: {local_value}")


if __name__ == "__main__":
    t1 = threading.Thread(target=worker, args=("thread-1",))
    t2 = threading.Thread(target=worker, args=("thread-2",))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("final global_value:", global_value)
