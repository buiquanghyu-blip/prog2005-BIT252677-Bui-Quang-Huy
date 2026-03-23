import math
lst = [2, 3, 5, 7, 10]
print("Danh sách ban đầu:", lst)

lst.append(int(input("Nhập phần tử cần thêm: ")))
print("Danh sách sau khi thêm:", lst)

k = int(input("Nhập giá trị k: "))
count_k = lst.count(k)
print(f"Số lần xuất hiện của {k}:", count_k)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

sum_prime = sum(x for x in lst if is_prime(x))
print("Tổng các số nguyên tố trong danh sách:", sum_prime)

lst.sort()
print("Danh sách sau khi sắp xếp:", lst)
