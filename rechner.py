def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Test the functions
print(add(5, 3))   # Output: 8
print(subtract(10, 4)) # Output: 6
print(multiply(7, 2)) # Output: 14
print(divide(9, 3))   # Output: 3
print(divide(10, 0)) # Output: Error: Division by zero