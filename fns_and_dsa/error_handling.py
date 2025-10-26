num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

try:
    result = num1/num2
    print(f'Result is {result}')
except ZeroDivisionError:
    print("Error: You can't do that here.")