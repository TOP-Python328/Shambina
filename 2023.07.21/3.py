num=int(input())
sum=0
square=int(num**0.5)
for i in range(1,square+1):
    if i*i==num:
        sum+=i
    elif num%i==0:
        sum+=i+num/i
print(int(sum))

# 50
# 93