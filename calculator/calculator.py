while True:
    print("Options:")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")
    print("Enter '0' to end the program")
    
    user_input = input(": ")

    if user_input == "0":
        break
    elif user_input in ("+", "-", "*", "/"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if user_input == "+":
            result = num1 + num2
        elif user_input == "-":
            result = num1 - num2
        elif user_input == "*":
            result = num1 * num2
        elif user_input == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero")
                continue
        print("Result: " + str(result))
    else:
        print("Invalid input. Please enter a valid option.")
