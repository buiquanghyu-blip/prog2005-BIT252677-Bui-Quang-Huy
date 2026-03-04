text = input("Nhập một chuỗi: ")

processed_text = text.replace(" ", "").lower()

if processed_text == processed_text[::-1]:
    print("Chuỗi là Palindrome (đối xứng).")
else:
    print("Chuỗi không phải là Palindrome.")
