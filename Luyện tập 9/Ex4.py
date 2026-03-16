s = input("Nhập một chuỗi: ")

upper = lower = digit = special = space = vowel = consonant = 0

vowels = "aeiouAEIOU"

for char in s:
    if char.isupper():
        upper += 1
    if char.islower():
        lower += 1
    if char.isdigit():
        digit += 1
    if char.isspace():
        space += 1
    if char.isalpha():
        if char in vowels:
            vowel += 1
        else:
            consonant += 1
    if not char.isalnum() and not char.isspace():
        special += 1

print("Số chữ cái in hoa:", upper)
print("Số chữ cái in thường:", lower)
print("Số chữ số:", digit)
print("Số ký tự đặc biệt:", special)
print("Số ký tự khoảng trắng:", space)
print("Số nguyên âm:", vowel)
print("Số phụ âm:", consonant)
