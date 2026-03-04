numbers = list(map(int, input("Nhập các số cách nhau bởi dấu cách: ").split()))

found_number = None

for num in numbers:
    if num > 10:
        found_number = num
        break
if found_number is not None:
    print("Số đầu tiên lớn hơn 10 là:", found_number)
else:
    print("Không có số nào lớn hơn 10 trong danh sách.")
