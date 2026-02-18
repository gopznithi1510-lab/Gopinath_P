def calculator():
    try:
        print("\n---- Python Recursive Calculator ----")
        print("Operators: +  -  *  /  %  **")
        
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator: ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print("Result:", num1 + num2)

        elif operator == "-":
            print("Result:", num1 - num2)

        elif operator == "*":
            print("Result:", num1 * num2)

        elif operator == "/":
            print("Result:", num1 / num2)

        elif operator == "%":
            print("Result:", num1 % num2)

        elif operator == "**":
            print("Result:", num1 ** num2)

        else:
            print("Invalid operator!")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    except ValueError:
        print("Error: Invalid number entered!")

    except Exception as e:
        print("Unexpected Error:", e)

    # Ask user to continue (Recursion)
    finally:
        choice = input("\nDo you want to calculate again? (yes/no): ").lower()
        if choice == "yes":
            calculator()   # Recursive call
        else:
            print("Calculator exited.")


# Start the calculator
calculator()
