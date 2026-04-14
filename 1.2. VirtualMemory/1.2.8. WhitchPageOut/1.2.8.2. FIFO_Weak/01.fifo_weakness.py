from collections import deque

ram = deque(["A", "B", "C"])

# 최근 사용 상황을 가정
recently_used = ["A", "A", "A", "B"]

print("RAM:", list(ram))
print("recently used:", recently_used)

victim = ram.popleft()  # FIFO는 그냥 가장 먼저 들어온 것 제거
print("FIFO removes:", victim)
