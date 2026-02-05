n = input("Nhập số nguyên dương 5 chữ số: ")

if len(n) != 5 or not n.isdigit():
    print("Số nhập vào không hợp lệ!")
else:
    print("Chữ số lớn nhất là:", max(n))
