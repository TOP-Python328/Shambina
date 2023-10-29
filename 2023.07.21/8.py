n = int(input())

fib = 0
prev = 1
preprev = 0

for i in range(n):
    preprev = prev
    prev = fib
    fib = preprev + prev
    print(fib, end = " ")

# 1
# 1

# 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
