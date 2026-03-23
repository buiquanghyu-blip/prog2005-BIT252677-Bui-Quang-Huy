def giai_thua(n):
    if n == 0 or n == 1:   
        return 1
    return n * giai_thua(n - 1)

n = int(input("Nhập số n: "))

if n < 0:
    print("Không có giai thừa cho số âm!")
else:
    print("Giai thừa của", n, "là:", giai_thua(n))
