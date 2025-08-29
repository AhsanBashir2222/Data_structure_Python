def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b


def calculator():
    print("Welcome to Basic Calculator!")
    print("Operations: +, -, *, /")

    while True:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            result = "Invalid operator!"

        print("Result:", result)

        # Ask user if they want to continue
        choice = input(
            "Do you want to perform another calculation? (yes/no): ").lower()
        if choice != 'yes':
            print("Thank you for using the calculator!")
            break


# Run the calculator
calculator()
