operator = input("Enter an operator (+, -, *, /): ")

num1 = float(input("Enter the 1th number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == '+':
    result = round(num1 + num2, 3)
    print(f"{num1} + {num2} = {result}")
elif operator == '-':
    result = round(num1 - num2, 3)
    print(f"{num1} - {num2} = {result}")
elif operator == '*':
    result = round(num1 * num2, 3)
    print(f"{num1} * {num2} = {result}")
elif operator == '/':
    result = round(num1 / num2, 3)
    print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operator. Pleas use +, -, *, or /.")