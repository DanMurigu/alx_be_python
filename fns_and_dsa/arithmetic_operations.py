num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation: (add, subtract, multiply, divide): ").lower()

def perform_operation(num1, num2, operation):
    operation = operation.strip().lower()
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Number not divisible by zero"
        return num1 / num2
    else:
        return f"Error: Unsupported operation {operation}"
result = perform_operation(num1,num2, operation)
print(f"Result: {result}")