import math
try:
    n = float(input("Nhập một số: "))

    if n < 0:
        print("Lỗi: Không thể tính căn bậc hai của số âm.")
    else:
        sqrt_n = math.sqrt(n)
        print(f"Căn bậc hai của {n} là: {sqrt_n}")

except ValueError:
    print("Lỗi: Vui lòng nhập một số hợp lệ.")
