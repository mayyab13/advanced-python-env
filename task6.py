a = int(input("first number is: "))
operation = input("Choose operation (+, -, *, /): ")
b = int(input("Second number: "))

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    print(a / b)
else:
    print("Unknown operation")
