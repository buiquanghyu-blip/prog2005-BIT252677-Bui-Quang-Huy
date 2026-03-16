class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Lão Hạcccc")


d = Dog("Cậu Vàng")

print("Tên:", d.name)
d.sound()
