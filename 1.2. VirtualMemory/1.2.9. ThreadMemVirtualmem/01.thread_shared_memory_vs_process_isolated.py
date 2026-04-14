import multiprocessing
import threading

shared_value = 0


def thread_worker():
    global shared_value
    shared_value = 100


def process_worker():
    global shared_value
    shared_value = 999


if __name__ == "__main__":
    shared_value = 0
    t = threading.Thread(target=thread_worker)
    t.start()
    t.join()
    print("after thread:", shared_value)

    shared_value = 0
    p = multiprocessing.Process(target=process_worker)
    p.start()
    p.join()
    print("after process:", shared_value)
