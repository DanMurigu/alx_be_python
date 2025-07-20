num1 = "num1"
num2 = "num2"
operation = "(+, -, *, /)"

num1 = int(input("Enter the first number: " ))
num2 = int(input("Enter the second number: gi" ))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
      
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    
    case "/":
       if num2 == 0:
        print("Cannot divide by zero")
       else:
          result = num1 / num2
          print(f"The result is {result}.")
        
    case _:
        print("Invalid operation selected")
