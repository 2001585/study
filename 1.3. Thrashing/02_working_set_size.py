def get_working_set(page_sequence, window_size):
    for i in range(len(page_sequence)):
        window = page_sequence[max(0, i - window_size + 1) : i + 1]
        working_set = set(window)

        print(
            f"현재 요청: {page_sequence[i]}, "
            f"최근 {window_size}개 접근: {window}, "
            f"Working Set: {working_set}, "
            f"크기: {len(working_set)}"
        )


page_sequence = [1, 2, 3, 4, 1, 2, 3, 4]
get_working_set(page_sequence, window_size=4)
