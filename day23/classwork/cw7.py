# 7)მომხმარებელს შემოტანანინე წინადადება და სიმბოლო, საბოლოოდ იპოვე ამ წინადადებაში რომელ ინდექსებზე დგას ყველა ეს სიმბოლო (როგორც ჩვენ გავაკეთეთ)
sentence = input("შეიყვანეთ წინადადება: ")
symbol = input("შეიყვანეთ სიმბოლო: ")
indices = []
for i in range(len(sentence)):
    if sentence[i] == symbol:
        indices.append(i)
print(f"სიმბოლო {symbol} ინდექსებში დგას: {indices}")