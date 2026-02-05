n = int(input("Nhập số nguyên dương n: "))
tong = 0

if n <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    for i in range(1, n + 1):
        if i % 2 != 0:
            tong += i

    print("Tổng các số lẻ từ 1 đến", n, "là:", tong)
