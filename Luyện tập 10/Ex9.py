class Person:
    count = 0

    def __init__(self, name, age):
        self._name = name
        self.age = age
        Person.count += 1

    def get_name(self):
        return self._name

    def set_name(self, name):
        if not name:
            raise ValueError("Tên không được rỗng!")
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Tuổi phải >= 0!")
        self._age = value

    def __str__(self):
        return f"Person(name={self._name}, age={self._age})"

    def introduce(self):
        return f"Xin chào, tôi là {self._name}"

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def is_adult(age):
        return age >= 18

    def __eq__(self, other):
        return self._name == other._name and self._age == other._age


class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        if score < 0 or score > 10:
            raise ValueError("Điểm phải từ 0 đến 10!")

        self.score = score

    def __str__(self):
        return f"Student(name={self._name}, age={self._age}, score={self.score})"
    def study(self):
        return f"{self._name} đang học bài"

    def __eq__(self, other):
        return super().__eq__(other) and self.score == other.score

try:
    p1 = Person("Huy", 20)
    p2 = Person("An", 20)

    print(p1)
    print(p1.introduce())
    print("Số người:", Person.get_count())
    print("Có phải người lớn?", Person.is_adult(20))
    print("So sánh p1 == p2:", p1 == p2)

    print("\n--- Student ---")
    s1 = Student("Hưng", 18, 8.5)
    s2 = Student("Loong", 18, 8.5)

    print(s1)
    print(s1.study())
    print("So sánh s1 == s2:", s1 == s2)

except ValueError as e:
    print("Lỗi:", e)
