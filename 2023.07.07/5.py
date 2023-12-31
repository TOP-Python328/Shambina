# ПЕРЕИМЕНОВАТЬ: целая часть числа — integer: дробная часть числа — fractional (сокращения допустимы)
# КОММЕНТАРИЙ: div и mod — сокращения от названия операций (division и modulo)
div = input()
mod = input()
miles = float(div + '.' + mod)
km = miles * 1.61
print(f"{miles} миль = {km:.1f} км")


# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы после символа # — в большинстве редакторов кода, включая Notepad++, это делает команда "Вкл./Выкл. комментарий"
# 15
# 7
# 15.7 миль = 25.3 км


# ИТОГ: отлично — 5/5
