import time
#My First Python Project a basic calculator




while True:
    print("Type the first number you would like to use")
    firstNumber = int(input())
    print("Type the second number you would like to use")
    secondNumber = int(input())

    time.sleep(1.0)

    print("Would you like to Multiply (x), Divide (/), Add (+) or Subtract (-) the value?")
    category = input()

    if category == "Multiply" or "multiply" or "x" or ".":
        result = firstNumber * secondNumber
        print(f"Multiplying, {firstNumber} and {secondNumber}, is equal to, {result}")
    elif category == "Divide" or "divide" or "/":
        if secondNumber != 0:
            result = firstNumber / secondNumber
            print(f"Dividing, {firstNumber} and {secondNumber}, is equal to, {result}")
        else:
            print("ERROR: Cannot divide to ZERO")
    elif category == "Add" or "add" or "+":
        result = firstNumber + secondNumber
        print(f"Adding, {firstNumber} and {secondNumber}, is equal to,{result}")
    elif category == "Subtract" or "subtract" or "-":
        result = firstNumber - secondNumber
        print(f"Subtracting, {firstNumber} - {secondNumber}, is equal to, {result}")
    else:
        print("ERROR: Invalid Input")