
# As a challenge, try to expand your calculator :
# let the user enter as many numbers they want and perform the selected operation of all of them.
# Or, let the user enter more than just one operator and perform the operations on all supplied numbers.
# You can also practice your formatting
# - rather than printing just the result, print out all the operations in a neat way.

# Made input into a string, then split this string into a list.
# Looped through each item (number) in the list to perform the operation on each.
# chr(247) gives the division symbol

try2 = input("Would you like to try a calculation? Y/N ").upper()

while try2 == "Y":
    str1 = (input("Please input your numbers separated by the comma sign ',': "))
    operator = input("Which operator would you like to use? ")
    num2 = float(input("Which number would you like to perform this operation with? "))
    str2 = str1.split(',')
    if num2 == 0 and operator == "/":
        print("Sorry, you cannot divide by 0.")
    else:
        for number in str2:
            if operator == "+":
                print(number, '+', num2, '=', str(round(float(number) + num2, 2)))
            elif operator == "-":
                print(number, '-', num2, '=', str(round(float(number) - num2, 2)))
            elif operator == "*":
                print(number, 'x', num2, '=', str(round(float(number) * num2, 2)))
            elif operator == "/":
                print(number, chr(247), num2, '=', str(round(float(number) / num2, 2)))
            else:
                print("Sorry, you must input one of the following operators: +, -, *, / ")
    try2 = input("Would you like to try another calculation? Y/N ").upper()

else:
    print("Thank you for using this python calculator!")
