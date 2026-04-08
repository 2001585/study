page_table = {
    0: 5,
    1: 12,
    2: 2,
    3: 9,
}

virtual_page = 2
physical_frame = page_table[virtual_page]

print(f"virtual page {virtual_page} -> physical frame {physical_frame}")
