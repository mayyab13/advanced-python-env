a = int(input("First number: "))
op = input("Operation: ")
b = int(input("Second number: "))

if op == "/" and b == 0:
    print("Cannot divide by zero")
elif op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Wrong operation")
