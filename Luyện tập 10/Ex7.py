mat_khau_dung = "python123"

while True:
    nhap = input("Nhập mật khẩu: ")

    if nhap == mat_khau_dung:
        print("Đăng nhập thành công!")
        break
    else:
        print("Sai mật khẩu, thử lại!")
