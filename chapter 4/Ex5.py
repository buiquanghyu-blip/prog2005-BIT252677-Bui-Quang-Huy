class Product:
    def __init__(self, price):
        self._price = price
    def get_price(self):
        return self._price

    def set_price(self, price):
        if price > 0:
            self._price = price
        else:
            print("Giá phải lớn hơn 0")

    def __str__(self):
        return f"Price của product: {self._price}"

p1 = Product(100)

p1.set_price(200)

print(p1)
