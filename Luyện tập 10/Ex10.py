ds = []
for i in range(5):
    s = input(f"Nhập chuỗi {i + 1}: ")
    ds.append(s)

print("\nDanh sách ban đầu:", ds)

n = len(ds)
step = 1

for i in range(n - 1):
    for j in range(n - i - 1):
        if len(ds[j]) < len(ds[j + 1]):
            ds[j], ds[j + 1] = ds[j + 1], ds[j]

            print(f"Bước {step}: {ds}")
            step += 1

print("\nDanh sách sau khi sắp xếp:", ds)
