numbers = input().split()

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

max_salary = a
if b > max_salary:
    max_salary = b
if c > max_salary:
    max_salary = c

min_salary = a
if b < min_salary:
    min_salary = b
if c < min_salary:
    min_salary = c

print(max_salary - min_salary)
