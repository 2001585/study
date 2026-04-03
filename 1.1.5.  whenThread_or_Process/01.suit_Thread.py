import threading
import time


def save_log():
    for i in range(3):
        print("로그 저장 중...", i)
        time.sleep(1)


t = threading.Thread(target=save_log)
t.start()

print("메인 작업 계속 수행")
t.join()
print("종료")
