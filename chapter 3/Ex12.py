m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

def nhap_ma_tran(ten):
    print(f"Nhập ma trận {ten}:")
    matrix = []
    for i in range(m):
        while True:
            row = list(map(int, input(f"Hàng {i+1}: ").split()))
            if len(row) == n:
                matrix.append(row)
                break
            else:
                print("⚠ Vui lòng nhập đúng", n, "phần tử!")
    return matrix

A = nhap_ma_tran("A")
B = nhap_ma_tran("B")

C = [[A[i][j] + B[i][j] for j in range(n)] for i in range(m)]

print("Ma trận tổng C = A + B:")
for row in C:
    print(*row)
