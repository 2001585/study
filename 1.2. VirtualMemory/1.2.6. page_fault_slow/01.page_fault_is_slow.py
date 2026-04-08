# 07_page_fault_is_slow.py
import time

page_table = {
    0: 3,
    1: 7,
}

def access_page(page):
    start = time.time()

    if page in page_table:
        print(f"page {page}: RAM에 있음")
    else:
        print(f"page {page}: 페이지 폴트 발생")
        time.sleep(1)  # 디스크에서 가져오는 느린 상황을 단순 흉내
        page_table[page] = 5
        print(f"page {page}: 디스크에서 읽어와 RAM에 적재 완료")

    end = time.time()
    print("elapsed:", round(end - start, 3), "seconds")


access_page(1)
access_page(2)