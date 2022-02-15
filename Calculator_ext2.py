
# Let the user enter more than just one operator and perform the operations on all supplied numbers.

# chr(247) gives the division symbol

# This calculator can perform further operations on the returned value after each operation is performed.
# The user can choose to exit the loop by typing 'X' instead of another operator.
# The variable 'num1' is reassigned as the result to allow further operations to be performed.

print("Welcome to Calculator Extension 2.")
num1 = float(input("Input number: "))
operator = input("Input operator: ")
num2 = float(input("Input number: "))

while operator != 'X':
    if num2 == 0 and operator == "/":
        print("Sorry, you cannot divide by 0.")
    else:
        if operator == "+":
            ans = str(round(float(num1) + num2, 2))
            print(num1, '+', num2, '=', ans)
            num1 = ans
        elif operator == "-":
            ans = str(round(float(num1) - num2, 2))
            print(num1, '-', num2, '=', ans)
            num1 = ans
        elif operator == "*":
            ans = str(round(float(num1) * num2, 2))
            print(num1, 'x', num2, '=', ans)
            num1 = ans
        elif operator == "/":
            ans = str(round(float(num1) / num2, 2))
            print(num1, chr(247), num2, '=', ans)
            num1 = ans
        else:
            print("Sorry, you must input one of the following operators: +, -, *, / ")
    operator = input("Another operator? (You may type X to exit):")
    if operator == 'X':
        print("Thank you for using this python calculator!")
        break
    num2 = float(input("Input number: "))
else:
    print("Thank you for using this python calculator!")
