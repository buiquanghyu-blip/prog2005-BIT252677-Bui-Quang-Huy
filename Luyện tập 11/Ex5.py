my_dict = {"a": 1, "b": 2, "c": 3}
key = input("Nhập key cần kiểm tra: ")

if key in my_dict:
    print(f"Key '{key}' tồn tại với giá trị {my_dict[key]}")
else:
    print(f"Key '{key}' không tồn tại")
