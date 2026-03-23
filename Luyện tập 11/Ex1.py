def insertion_sort_descending(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and len(key) > len(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Bước {i}: {arr}")
    return arr

strings = []
for i in range(5):
    strings.append(input(f"Nhập chuỗi thứ {i+1}: "))

print("\nQuá trình sắp xếp:")
sorted_strings = insertion_sort_descending(strings)
print(f"Kết quả cuối cùng: {sorted_strings}")
