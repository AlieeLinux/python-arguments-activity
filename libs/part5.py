"""
Part 5 — Mini Challenge (Calculator)
Create a function:
def compute(operation, num1, num2=1):
    • If operation == "add" → return sum
    • If "multiply" → return product
    • If "subtract" → return difference
    • Else → return "Invalid operation"
Tasks:
    1. compute("add", 5, 10)
    2. compute("multiply", num1=3, num2=4)
    3. compute("subtract", 20) (use default)
    4. Try an invalid operation.
"""

def compute(operation, num1, num2=1):
    if operation == "add":
        return num1 + num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "subtract":
        return num1 - num2
    else:
        return "Invalid Operation"

