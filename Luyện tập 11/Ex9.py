rows = int(input("Số hàng: "))
cols = int(input("Số cột: "))

A = []
print("Nhập ma trận A:")
for i in range(rows):
    row = input(f"Hàng {i+1} (cách nhau bởi dấu cách): ").split()
    if len(row) != cols or "" in row:
        print("Lỗi: số lượng giá trị không đúng hoặc giá trị trống")
        exit()
    A.append([int(x) for x in row])

B = []
print("Nhập ma trận B:")
for i in range(rows):
    row = input(f"Hàng {i+1} (cách nhau bởi dấu cách): ").split()
    if len(row) != cols or "" in row:
        print("Lỗi: số lượng giá trị không đúng hoặc giá trị trống")
        exit()
    B.append([int(x) for x in row])

C = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
print("Ma trận tổng:")
for row in C:
    print(row)
