first = input()
second = input()

first_list = list(int(el) for el in first.split())
second_list = list(int(el) for el in second.split())

subset = "нет"
for i in range(len(second_list)):
    if first_list[i] == second_list[i]:
        continue
    else:
        break
else:
    subset = "да"

print(subset)

# 1 2 3 4 5 6 7 8 9
# 1 2 3 4
# да

# 1 2 3 4
# 2 4
# нет
