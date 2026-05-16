# Functions for all operations first

def add(a,b):
    return a+b 

def subtract(a,b):
    return a-b 

def multiply(a,b):
    return a*b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# User Inputs

a = float(input(('Enter a number')))

operation = input("Choose operation (+, -, *, /): ")

b = float(input(("Enter the second number")))

# Operations

if operation == "+":
    print(add(a,b))  

elif operation == "-":
    print(subtract(a,b))

elif operation == "*":
    print(multiply(a,b))
elif operation == "/":
    print(divide(a,b))  
else: 
    print("Invalid operation. Please choose +, -, *, or /")