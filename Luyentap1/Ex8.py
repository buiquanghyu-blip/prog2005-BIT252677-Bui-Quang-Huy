class Student:
    def __init__(self, name, score):
        self.name = name

        if 0 <= score <= 10:
            self.score = score
        else:
            print("Điểm không hợp lệ! Điểm phải nằm trong khoảng 0–10.")
            self.score = 0


student1 = Student("Nam", 8.5)
student2 = Student("Lan", 77)

print(student1.name, "-", student1.score)
print(student2.name, "-", student2.score)
