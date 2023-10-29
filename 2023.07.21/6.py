num = int(input())

summa_first = 0
summa_second = 0

for i in range(6):
    n = num % 10
    num = num // 10

    if i < 3:
        summa_second += n
    else:
        summa_first += n
        
if summa_first == summa_second:
    print("да")
else:
    print("нет")

# 183534
# да

# 401367
# нет
