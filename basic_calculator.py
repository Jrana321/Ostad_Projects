
""" basic calculator program using Python
 Developed by-
 Md Atiqur Rahman

 """

"""Function Definitions """

def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers."""
    try:
        return x / y
    #except ZeroDivisionError:
    except Exception as e:
        print(f"Error: Cannot divide by zero.({e} found)")
        return None

def modulus(x, y):
    """Calculates the modulus of two numbers."""
    return x % y
#### Implement User Input Handling####
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

choice = input("Enter choice (1/2/3/4/5): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

try:
 if choice == '1':
    print(f"Addition:{num1} + {num2} = {add(num1, num2)}")
 elif choice == '2':
    print(f"subtraction:{num1} - {num2} = {subtract(num1, num2)}")
 elif choice == '3':
    print(f"Multiplication:{num1} * {num2} = {multiply(num1, num2)}")
 elif choice == '4':
    result = divide(num1, num2)
    if result is not None:
        print(f"Division:{num1} / {num2} = {result}")
 elif choice == '5':
    print(f"Modulus:{num1} % {num2} = {modulus(num1, num2)}")
 else:
    print("Invalid input")
except  Exception as s:
    print("Error:",s)


