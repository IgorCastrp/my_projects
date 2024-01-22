def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2

number1 = float(input("Choose the 1st number: "))
operation = int(input("1. +\n2. -\n3. /\n4. *\nChoose the number: "))
number2 = float(input("Choose the 2nd number: "))

if operation == 1:
    result = add(number1, number2)
    print(f"The result is: {result}")
elif operation == 2:
    result = subtract(number1, number2)
    print(f"The result is: {result}")
elif operation == 3:
    result = divide(number1, number2)
    print(f"The result is: {result}")
elif operation == 4:
    result = multiply(number1, number2)
    print(f"The result is: {result}")
else:
    print("Operation not valid")


