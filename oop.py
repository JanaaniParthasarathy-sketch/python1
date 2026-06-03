#1st

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

s1 = Student("Janaani", 18)
s1.display()

#encapsulation
class Bank:
    def __init__(self):
        self.balance = 1000

    def show_balance(self):
        print(self.balance)

obj = Bank()
obj.show_balance()


#class inheritance
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()

d.sound()
d.bark()

#method overrinding
class Animal:
    def sound(self):
        print("Animal Sound")

class Cat(Animal):
    def sound(self):
        print("Meow")

c = Cat()
c.sound()

#full program

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

class Manager(Employee):
    def display_role(self):
        print("Role: Manager")

emp = Manager("Rahul", 50000)

emp.display()
emp.display_role()
