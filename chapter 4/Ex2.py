students = {
    "Hưng": 8.5,
    "Hùng": 9.0,
    "Huy": 9.5
}

def tinh_diem_trung_binh(ds):
    tong = 0
    so_sv = len(ds)

    for diem in ds.values():
        tong += diem

    return tong / so_sv

dtb = tinh_diem_trung_binh(students)

print("Điểm trung bình của các sinh viên:", dtb)
