import time


def run_program(page_fault_count, compute_count):
    start = time.time()

    for i in range(compute_count):
        print(f"계산 수행: {i + 1}")

    for i in range(page_fault_count):
        print(f"페이지 폴트 처리 대기: {i + 1}")
        time.sleep(0.5)

    end = time.time()
    print(f"\n전체 실행 시간: {end - start:.2f}초")


print("상황 A: 페이지 폴트가 적은 경우")
run_program(page_fault_count=1, compute_count=5)

print("\n" + "=" * 50 + "\n")

print("상황 B: 페이지 폴트가 많은 경우")
run_program(page_fault_count=6, compute_count=5)
