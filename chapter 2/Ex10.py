def tong(n):
    if n == 1:
        return 1
    return n + tong(n - 1)

n = int(input("Nhập số nguyên dương n: "))

if n <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    print("Tổng từ 1 đến", n, "là:", tong(n))
