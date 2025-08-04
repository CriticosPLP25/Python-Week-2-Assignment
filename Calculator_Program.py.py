#This program is a simple calculator 
# It prompts a user to enter two numbers and an arithmetic operator 
# It then performs basic arithmetic operations based on the input.

# User input for numbers and operator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")

# Performing the operation based on the operator input
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Can't divide by zero."
else:
    result = "Error! Enter correct operator."

# Output the result
print(result)
# End of Calculator Program