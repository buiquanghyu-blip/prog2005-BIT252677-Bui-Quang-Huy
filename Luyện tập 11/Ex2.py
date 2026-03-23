def binary_search(arr, target_len):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if len(arr[mid]) == target_len:
            return mid
        elif len(arr[mid]) < target_len: 
            high = mid - 1
        else:
            low = mid + 1
    return -1

search_str = input("\nNhập chuỗi cần tìm vị trí theo độ dài: ")
index = binary_search(sorted_strings, len(search_str))

if index != -1:
    print(f"Chuỗi có độ dài tương đương nằm ở vị trí (index): {index}")
else:
    print("Không tìm thấy chuỗi có độ dài này.")
