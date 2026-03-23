info = {}
n = int(input("Nhập số lượng người: "))
for _ in range(n):
    name = input("Nhập tên: ")
    age = int(input("Nhập tuổi: "))
    info[name] = age

average_age = sum(info.values()) / len(info)
print("Thông tin:", info)
print("Tuổi trung bình:", average_age)
