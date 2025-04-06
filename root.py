import math

def calculate_square_root(number):
    if number < 0:
        return "Cannot compute the square root of a negative number."
    return math.sqrt(number)

# Get user input
num = float(input("Enter a number to find its square root: "))
result = calculate_square_root(num)
print(f"The square root of {num} is: {result}")
