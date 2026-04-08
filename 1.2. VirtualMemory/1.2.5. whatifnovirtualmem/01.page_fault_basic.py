# 06_page_fault_basic.py

page_table = {
    0: 3,
    1: 7,
    # 2는 아직 RAM에 없다고 가정
}

virtual_page = 2

if virtual_page in page_table:
    print("RAM에 있음")
    print("frame:", page_table[virtual_page])
else:
    print("페이지 폴트 발생!")
    print("디스크에서 페이지를 가져와야 함")