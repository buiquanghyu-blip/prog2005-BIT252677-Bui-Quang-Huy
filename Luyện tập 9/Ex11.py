class SinhVien:
    count = 0

    def __init__(self, ten):
        self.ten = ten
        SinhVien.count += 1   

    @classmethod
    def dem_so_sinh_vien(cls):
        return cls.count


sv1 = SinhVien("Huy")
sv2 = SinhVien("Hùng")
sv3 = SinhVien("Hưng")

print("Số sinh viên đã tạo:", SinhVien.dem_so_sinh_vien())
