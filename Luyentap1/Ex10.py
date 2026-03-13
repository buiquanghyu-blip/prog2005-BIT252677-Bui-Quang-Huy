def add_product():
    code = input("Nhập mã sản phẩm: ")
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập giá sản phẩm: "))

    with open("products.txt", "a", encoding="utf-8") as f:
        f.write(f"{code};{name};{price}\n")


def show_products():
    products = []

    with open("products.txt", "r", encoding="utf-8") as f:
        for line in f:
            code, name, price = line.strip().split(";")
            products.append((code, name, float(price)))

    print("\nDanh sách sản phẩm:")
    for p in products:
        print(p[0], "-", p[1], "-", p[2])

    return products


def sort_products(products):
    products.sort(key=lambda x: x[2], reverse=True)

    print("\nSản phẩm sau khi sắp xếp theo giá giảm dần:")
    for p in products:
        print(p[0], "-", p[1], "-", p[2])


add_product()
products = show_products()
sort_products(products)
