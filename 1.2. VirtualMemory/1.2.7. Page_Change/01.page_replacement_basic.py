# 08_page_replacement_basic.py

ram_frames = ["A", "B", "C"]
new_page = "D"

print("before:", ram_frames)

victim_index = 1  # 예시로 B를 교체 대상으로 선택
victim_page = ram_frames[victim_index]

print("remove page:", victim_page)
ram_frames[victim_index] = new_page

print("load page:", new_page)
print("after:", ram_frames)
