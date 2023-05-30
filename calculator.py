def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Cannot divide by zero."

def calculator():
    print("Welcome to the Calculator!")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    while True:
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = add(num1, num2)
            print(f"The result is: {result}")
        elif choice == "2":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = subtract(num1, num2)
            print(f"The result is: {result}")
        elif choice == "3":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = multiply(num1, num2)
            print(f"The result is: {result}")
        elif choice == "4":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = divide(num1, num2)
            print(f"The result is: {result}")
        elif choice == "5":
            print("Thank you for using the Calculator!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    calculator()