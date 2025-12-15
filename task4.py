N = int(input())

if N >= 1:
    result = sum(range(1, N + 1))
else:
    result = sum(range(N, 2))

print(result)
