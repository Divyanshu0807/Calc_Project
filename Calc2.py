import Addition
import Subtraction
import Multiplication
import Division
import Power

print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")

while True:
    # Take input from the user
    ch = input("Enter choice(1/2/3/4/5): ")

    # Check if choice is one of the four options
    if ch in ('1', '2', '3', '4','5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if ch == '1':
            print("Addition")
            print(num1, "+", num2, "=", Addition.add(num1, num2))

        elif ch == '2':
            print("Subtraction")
            print(num1, "-", num2, "=", Subtraction.subtract(num1, num2))

        elif ch == '3':
            print("Multiplication")
            print(num1, "*", num2, "=", Multiplication.multiply(num1, num2))

        elif ch == '4':
            print("Division")
            try:
                print(num1, "/", num2, "=", Division.divide(num1, num2))
            except ZeroDivisionError:
                print("Division by zero is not possible")
        elif ch=='5':
            print("Power")
            print(num1, "**", num2, "=", Power.power(num1,num2))
        # Check if user wants another calculation
        # Break the while loop if answer is no
        next_calc = input("Do you want to continue? (Yes/No): ")
        if next_calc in ("No","no"):
          break
    else:
        print("Invalid Input")
