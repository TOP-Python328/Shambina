fruit = "qwerty"
fruits_str = ""
fruits = []

while fruit:
    fruit = input()
    if fruit:
        fruits.append(fruit)

last = fruits.pop()
if len(fruits) >= 2:
    fruits_str = ", ".join(fruits) + " и " + last
elif len(fruits) == 0:
    fruits_str = last
elif len(fruits) == 1:
    fruits_str = fruits[0] + " и " + last

print(fruits_str)

# яблоко

# яблоко


# яблоко
# лимон

# яблоко и лимон


# яблоко
# банан
# апельсин
# лимон

# яблоко, банан, апельсин и лимон
