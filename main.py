
print("================================")
print("        PYTHON CALCULATOR")
print("================================")
print(" 1. Addition")
print(" 2. Substraction")
print(" 3. Multiplication")
print(" 4. Division")
print(" 5. Exit")

choice = input("Enter your choice (1/2/3/4/5): ")

if choice == "1":
    num1 = float(input("enter your first number:"))
    num2 = float(input("enter your second number:"))
    result = num1 + num2
    print("The result of the addition is:", result)
elif choice == "2":
    num1 = float(input("eneter your first number:"))
    num2 = float(input("enter your second number:"))
    result = num1 - num2
    print("the result of the subtraction is:",result)
elif choice == "3":
    num1 = float(input("enter your first number:"))
    num2 = float(input("enter your second number:"))
    result = num1 * num2
    print("Result of the mutiplication:",result)
elif choice == "4":
    num1 = float(input("enter your first number:"))
    num2 = float(input("enter your second number:"))
    if num2 == 0:
        print("error: Division by Zero is not allowed")
    else:
        result = num1/num2
        print("Result of Division:",result)
elif choice == "5":
    print("Exiting calculator...")
else:
    print("invalid choice. please select a valid option (1/2/3/4/5).")
