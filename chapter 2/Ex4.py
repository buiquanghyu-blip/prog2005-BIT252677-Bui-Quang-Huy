n = input("Nhập một số: ")

tong = 0
for ch in n:
    if ch.isdigit():
        tong += int(ch)

print("Tổng các chữ số là:", tong)
