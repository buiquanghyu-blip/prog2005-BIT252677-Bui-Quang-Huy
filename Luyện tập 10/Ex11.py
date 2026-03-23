def dao_chuoi():
    s = input("Nhập chuỗi: ")
    kq = ""
    for c in s:
        kq = c + kq
    print("Chuỗi đảo:", kq)

def dem_ky_tu():
    s = input("Nhập chuỗi: ")
    k = input("Nhập ký tự: ")
    print("Số lần xuất hiện:", s.count(k))

def giai_thua():
    def gt(n):
        if n <= 1:
            return 1
        return n * gt(n - 1)

    n = int(input("Nhập n: "))
    if n < 0:
        print("Không hợp lệ!")
    else:
        print("Giai thừa:", gt(n))

def do_dai_chuoi():
    s = input("Nhập chuỗi: ")
    if s.strip() == "":
        print("Chuỗi rỗng!")
    else:
        print("Độ dài:", len(s))

while True:
    print("\n===== MENU =====")
    print("1. Đảo chuỗi")
    print("2. Đếm ký tự")
    print("3. Tính giai thừa")
    print("4. Độ dài chuỗi")
    print("0. Thoát")

    chon = input("Chọn chức năng: ")

    if chon == "1":
        dao_chuoi()
    elif chon == "2":
        dem_ky_tu()
    elif chon == "3":
        giai_thua()
    elif chon == "4":
        do_dai_chuoi()
    elif chon == "0":
        print("Thoát chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ!")
