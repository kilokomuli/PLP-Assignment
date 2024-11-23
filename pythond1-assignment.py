#  Python program that asks the user to input two numbers and a mathematical
# operation  (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.

def calculator():
    print("Welcome to the Basic Calcultor!")
    try:
        # get user input
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        #perform the calculation
        if operation == "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Error: Invalid operation. Please choose +, -, *, or /.")
    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the calculator
calculator()