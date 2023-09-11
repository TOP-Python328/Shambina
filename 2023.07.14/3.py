year=int(input())
if year%400==0:
    print("да")
elif year%100 != 0:
    if year%4==0:
        print("да")
    else:
        print("нет")
else:
    print("нет")
    
#2020
#да

#2021
#нет

#2024
#да

#400
#да

#500
#нет

#800
#да