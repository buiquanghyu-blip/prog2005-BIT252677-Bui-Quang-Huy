import csv

name = input("Tên nhân viên: ")
age = input("Tuổi: ")
emp_id = input("ID: ")

with open("nhanvien.txt", "w", encoding="utf-8") as f:
    f.write(f"{name};{age};{emp_id}\n")

with open("nhanvien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Tên", "Tuổi", "ID"])
    writer.writerow([name, age, emp_id])

print("Đã lưu thông tin vào file 'nhanvien.txt' và 'nhanvien.csv'")
