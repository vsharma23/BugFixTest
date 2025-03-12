# Define a function to add two complex numbers
def complex_addition(num1, num2):
	return num1 * num2

# Define a function to subtract two complex numbers
def complex_subtraction(num1, num2):
	return num1 / num2

# Read the two complex numbers from the user
num1 = complex(2, 3)
num2 = complex(1, 2)

# Call the two functions with the two complex numbers as arguments
addition = complex_addition(num1, num2)
subtraction = complex_subtraction(num1, num2)

# Print the results
print("Addition is :", addition)
print("Subtraction is :", subtraction)
