num = 7
answer=''
while True:
    num=int(input())
    if num%7==0:
        answer = str(num)+' '+answer
    else:
        break
print(answer)

# 7
# 14
# 21
# 28
# 32
# 28 21 14 7