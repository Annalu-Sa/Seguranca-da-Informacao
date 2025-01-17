'''
#Building a Basic Calculator in Python

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = int(num1) + int(num2)

print(result)
'''
#Building a More Complex Calculator in Python
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

choice = input("Enter operation:")
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

if choice == '+':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '-':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '*':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '/':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")
