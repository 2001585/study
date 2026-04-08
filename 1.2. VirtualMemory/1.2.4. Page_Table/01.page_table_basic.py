# 04_page_table_basic.py

PAGE_SIZE = 100
virtual_address = 270

page_table = {
    0: 3,
    1: 7,
    2: 5,
}

page_number = virtual_address // PAGE_SIZE
offset = virtual_address % PAGE_SIZE

frame_number = page_table[page_number]
physical_address = frame_number * PAGE_SIZE + offset

print("virtual address:", virtual_address)
print("page number:", page_number)
print("offset:", offset)
print("frame number:", frame_number)
print("physical address:", physical_address)