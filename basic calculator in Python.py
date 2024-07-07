# Define a function to perform the calculations
def calculate(num1, operator, num2):
    # Check the operator and perform the appropriate calculation
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        # Check if the second number is zero to avoid division by zero error
        if num2 == 0:
            return "Error: Cannot divide by zero"
        else:
            return num1 / num2
    else:
        # Handle invalid operators
        return "Error: Invalid operator"

# Get user input for the numbers and operator
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Call the calculate function with the user input
result = calculate(num1, operator, num2)

# Print the result
print("Result: ", result)