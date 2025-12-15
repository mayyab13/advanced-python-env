number = float(input())

integer_part = int(number)
fractional_part = number - integer_part

new_number = fractional_part * 100 + integer_part / 100

print(new_number)
