# Inheritance in Python

from re import X


class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("\nName:", self.name)
        print("Age:", self.age)

class cat(human):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def display(self):
        super().display()
        print("Color:", self.color, "\n")

z = human("Criz", 25)
z.display()

X = cat("Kurizu", 10, "Black")
X.display()