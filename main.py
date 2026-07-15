# =====================================
# Python Calculator
# Created by: Sushanth
# Version: 1.1
# =====================================
def add(num1: float, num2: float) -> float:
    return num1 + num2

def subtract(num1: float, num2: float) -> float: 
    return num1 - num2 

def multiply(num1: float, num2: float) -> float: 
    return num1 * num2 

def divide(num1: float, num2: float) -> float | str:  
    if num2 == 0:
        return "error: division by zero"
    else:
        return num1 / num2 
    
history: list[str] = []
    

while True:
    print("\n================================")
    print("        PYTHON CALCULATOR")
    print("================================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid input, please enter a valid number.")
        else:
            result = add(num1,num2)
            print(f"Result: {result}")

            history.append(f"{num1} + {num2} = {result}") 

    elif choice == "2":
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid input, please enter a valid number.")
        else:
            result = subtract(num1,num2)
            print(f"Result: {result}")

            history.append(f"{num1} - {num2} = {result}")

    elif choice == "3":
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid input, please enter a valid number.")
        else:
            result = multiply(num1,num2)
            print(f"Result: {result}")

            history.append(f"{num1} * {num2} = {result}")

    elif choice == "4":
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid input, please enter a valid number.")
        else:
            result = divide(num1,num2)
            print(f"Result: {result}")

            history.append(f"{num1} / {num2} = {result}")

    elif choice == "5":
        print("Exiting calculator...")
        break

    else:
        print("Invalid choice. Please enter 1-5.")

    
