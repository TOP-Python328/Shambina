import math

telegramm = input()
cost = 0
for letter in telegramm:
    if letter.isalpha() or letter.isdigit():
        cost += 0.3

int_cost = math.trunc(cost)
reminder = round((cost - int_cost)*100)
print(f"{int_cost} руб. {reminder} коп.")

# грузите апельсины бочках братья карамазовы
# 11 руб. 40 коп.