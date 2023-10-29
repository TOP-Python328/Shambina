email = input()
is_correct = "нет"
parts = []

if "@" in email:
    parts = email.split("@")
    if "." in parts[1]:
        is_correct = "да"
        
print(is_correct)

# sgd@ya.ru
# да

# abcde@fghij
# нет
