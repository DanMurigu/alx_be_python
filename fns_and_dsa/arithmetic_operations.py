num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation: (add, subtract, multiply, divide): ").lower()
#above are the user inputs
def perform_operation(num1, num2, operation): #the function that performs the arithmetic operations
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
result = perform_operation(num1,num2, operation) #included this to see if the function is working as expected
print(f"Result: {result}") #gives the output of the function