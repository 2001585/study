from collections import deque

ram = deque(["A", "B", "C"])
new_page = "D"

print("before:", list(ram))

victim = ram.popleft()  # 가장 먼저 들어온 페이지 제거
print("remove:", victim)

ram.append(new_page)  # 새 페이지 추가
print("load:", new_page)

print("after:", list(ram))
