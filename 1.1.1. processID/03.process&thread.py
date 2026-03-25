import os
import threading

print("프로세스 ID:", os.getpid())
print("현재 스레드:", threading.current_thread().name)
