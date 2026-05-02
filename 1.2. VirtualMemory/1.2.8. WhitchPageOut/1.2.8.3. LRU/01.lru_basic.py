ram = ["A", "B", "C"]

# 왼쪽이 가장 오래 전에 사용, 오른쪽이 가장 최근 사용
recent_order = ["B", "C", "A"]

new_page = "D"

print("RAM:", ram)
print("usage order:", recent_order)

victim = recent_order[0]  # 가장 오래 사용되지 않은 페이지
print("LRU removes:", victim)

ram.remove(victim)
ram.append(new_page)

print("after:", ram)
