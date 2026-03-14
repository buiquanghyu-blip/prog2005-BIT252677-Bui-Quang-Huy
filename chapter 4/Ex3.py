students = {
    "Hưng": 8.5,
    "Hùng": 9.0,
    "Huy": 9.5
}

ten = input("Nhập tên sinh viên cần kiểm tra: ")

if ten in students:
    print("Key tồn tại trong dictionary")
else:
    print("Key không tồn tại trong dictionary")
