# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы вокруг бинарных операторов
c1 = input()
c2 = input()
# ИСПОЛЬЗОВАТЬ: скобки избыточны — приоритет оператора or ниже чем приоритет любого оператора сравнения
# ИСПОЛЬЗОВАТЬ везде: круглые скобки используются для литерала кортежа, изменения порядка вычисления выражений, вызова функций и записи составного выражения на нескольких строчках — больше нигде и никак
if c1[0] == c2[0] or c1[1] == c2[1]:
    print("да")
else:
    print("нет")


# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы после символа # — в большинстве редакторов кода, включая Notepad++, это делает команда "Вкл./Выкл. комментарий"
# d1
# e1
# да

# g5
# g1
# да

# a2
# c4
# нет
