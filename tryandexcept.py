#first
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")

#second
try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Invalid input")

