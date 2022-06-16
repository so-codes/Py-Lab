# Design a class that store the information of employee and display the same

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

E1 = Employee("Kurizu", 10000)
E1.display()

