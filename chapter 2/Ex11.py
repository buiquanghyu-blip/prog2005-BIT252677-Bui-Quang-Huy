diem = float(input("Nhập điểm trung bình: "))

if diem < 0 or diem > 10:
    print("Điểm không hợp lệ! Vui lòng nhập điểm từ 0 đến 10.")
elif diem >= 8:
    print("Xếp loại: Giỏi")
elif diem >= 6.5:
    print("Xếp loại: Khá")
elif diem >= 5:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")
