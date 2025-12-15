ticket = input()

a = int(ticket[0])
b = int(ticket[1])
c = int(ticket[2])
d = int(ticket[3])
e = int(ticket[4])
f = int(ticket[5])

sum1 = a + b + c
sum2 = d + e + f

if sum1 == sum2:
    print("yes")
else:
    print("no")
