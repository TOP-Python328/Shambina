simple=[2]
num=10**int(input())-1
for i in range(2,num+1):
    simple.append(i)


a=[True]*num

for i in range(2,int(num**0.5)+1):
    if a[i]:
        j=i**2
        while j<num:
            a[j]=False
            j=j+i
sum=0
for el in a:
    if el:
        sum += 1

# Вычитаем простые числа, принадлежащие диапазону с меньшими разрядами
num = (num +1) // 10 -1
for i in range(2,num+1):
    simple.append(i)


a=[True]*num

for i in range(2,int(num**0.5)+1):
    if a[i]:
        j=i**2
        while j<num:
            a[j]=False
            j=j+i
sum2=0
for el in a:
    if el:
        sum2 += 1


print(sum - sum2)

# 3
# 143