word = input().upper()

scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

score = 0

for letter in word:
    if letter == "Ё":
        letter = "Е"
    points = [point for point, letters in scores_letters.items() if letter in letters]
    score += sum(points)

print(score)

# синхрофазотрон
# 29

# ёжик
# 9
