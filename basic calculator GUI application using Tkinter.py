import tkinter as tk

# Define a function to perform the calculations
def calculate():
    # Get the numbers and operator from the input fields
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operator = entry_operator.get()

    # Check the operator and perform the appropriate calculation
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        # Check if the second number is zero to avoid division by zero error
        if num2 == 0:
            result = "Error: Cannot divide by zero"
        else:
            result = num1 / num2
    else:
        # Handle invalid operators
        result = "Error: Invalid operator"

    # Update the result label with the calculated value
    label_result.config(text="Result: " + str(result))

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the number and operator input fields
label_num1 = tk.Label(root, text="Enter the first number:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_operator = tk.Label(root, text="Enteran operator (+, -, *, /):")
label_operator.pack()
entry_operator = tk.Entry(root)
entry_operator.pack()

label_num2 = tk.Label(root, text="Enter the second number:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Create the calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack()

# Create the result label
label_result = tk.Label(root, text="Result: ")
label_result.pack()

# Start the main event loop
root.mainloop()