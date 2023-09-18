cell1 = input()
cell2 = input()
# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы вокруг бинарных операторов
h1 = 0
if cell1[0] == 'a':
    h1 = 1
elif cell1[0] == 'b':
    h1 = 2
elif cell1[0] == 'c':
    h1 = 3
elif cell1[0] == 'd':
    h1 = 4
elif cell1[0] == 'e':
    h1 = 5
elif cell1[0] == 'f':
    h1 = 6
elif cell1[0] == 'g':
    h1 = 7
elif cell1[0] == 'h':
    h1 = 8
v1 = int(cell1[1])

h2 = 0
if cell2[0] == 'a':
    h2 = 1
elif cell2[0] == 'b':
    h2 = 2
elif cell2[0] == 'c':
    h2 = 3
elif cell2[0] == 'd':
    h2 = 4
elif cell2[0] == 'e':
    h2 = 5
elif cell2[0] == 'f':
    h2 = 6
elif cell2[0] == 'g':
    h2 = 7
elif cell2[0] == 'h':
    h2 = 8
v2 = int(cell2[1])

if (h1 + v1) % 2 == (h2 + v2) % 2:
    print("да")
else:
    print("нет")


# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы после символа # — в большинстве редакторов кода, включая Notepad++, это делает команда "Вкл./Выкл. комментарий"
# a1
# a3
# да

# a1
# h1
# нет

