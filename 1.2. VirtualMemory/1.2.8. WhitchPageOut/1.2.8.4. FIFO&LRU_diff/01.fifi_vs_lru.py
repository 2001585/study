ram = ["A", "B", "C"]

fifo_order = ["A", "B", "C"]  # 들어온 순서
lru_order = ["B", "C", "A"]  # 사용 순서 (왼쪽이 가장 오래 전에 사용)

print("RAM:", ram)

fifo_victim = fifo_order[0]
lru_victim = lru_order[0]

print("FIFO removes:", fifo_victim)
print("LRU removes:", lru_victim)
