chuoi = input("Nhập chuỗi: ")

dao_nguoc = ""

for i in range(len(chuoi) - 1, -1, -1):
    dao_nguoc += chuoi[i]

print("Chuỗi đảo ngược:", dao_nguoc)
