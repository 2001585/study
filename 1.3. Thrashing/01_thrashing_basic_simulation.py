from collections import deque


def simulate_fifo(page_sequence, frame_count):
    frames = deque()
    page_faults = 0

    for page in page_sequence:
        if page not in frames:
            page_faults += 1
            if len(frames) < frame_count:
                frames.append(page)
            else:
                frames.popleft()
                frames.append(page)

        print(f"요청 페이지: {page}, 현재 프레임: {list(frames)}")

    return page_faults


page_sequence = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

faults_small = simulate_fifo(page_sequence, frame_count=3)

print(f"\nframe=3일 때 페이지 폴트 수: {faults_small}")

print("\n" + "=" * 50 + "\n")

faults_enough = simulate_fifo(page_sequence, frame_count=4)
print(f"\nframe=4일 때 페이지 폴트 수: {faults_enough}")
