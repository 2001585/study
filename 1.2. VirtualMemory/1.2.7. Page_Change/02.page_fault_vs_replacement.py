# 09_page_fault_vs_replacement.py

ram = ["A", "B", "C"]  # 프레임 3개가 모두 사용 중
needed_page = "D"

print("현재 RAM:", ram)
print("필요한 페이지:", needed_page)

if needed_page in ram:
    print("이미 RAM에 있음")
else:
    print("페이지 폴트 발생: 필요한 페이지가 RAM에 없음")

    if None in ram:
        empty_index = ram.index(None)
        ram[empty_index] = needed_page
        print("빈 프레임에 적재")
    else:
        victim_index = 1
        victim_page = ram[victim_index]
        print("페이지 교체 발생")
        print("내보내는 페이지:", victim_page)
        ram[victim_index] = needed_page
        print("새로 적재한 페이지:", needed_page)

print("최종 RAM:", ram)
