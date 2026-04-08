PAGE_SIZE = 4096
virtual_address = 9000

page_number = virtual_address // PAGE_SIZE
offset = virtual_address % PAGE_SIZE

print("virtual address:", virtual_address)
print("page number:", page_number)
print("offset:", offset)