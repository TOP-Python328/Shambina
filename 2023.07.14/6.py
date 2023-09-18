# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы вокруг бинарных операторов
c1 = input()
c2 = input()

vert_ok = False
horiz_ok = False

if abs(int(c1[1]) - int(c2[1])) < 2:
    vert_ok = True
if abs(ord(c1[0]) - ord(c2[0])) < 2:
    horiz_ok = True

if vert_ok and horiz_ok:
    print("да")
else:
    print("нет")


# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы после символа # — в большинстве редакторов кода, включая Notepad++, это делает команда "Вкл./Выкл. комментарий"
# a1
# b1
# да

# a1
# c1
# нет

# b2
# d3
# нет

