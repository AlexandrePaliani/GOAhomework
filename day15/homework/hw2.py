
# 2)ცვლადში შეინახეთ თქვენი საყვარელი რიცხვი და მომხმარებელს შემოატანინეთ ასევე მისი საყვარელი რიცხვი, თუ თქვენი რიცხვები ემთხვევა მაშინ დაბეჭდეთ "Perfect" თუ მისი რიცხვი მეტია, დაბეჭდეთ "More", სხვა შემთხვევაში "Less".

my_favorite_number = 67
user_favorite_number = int(input("შეიყვანეთ თქვენი საყვარელი რიცხვი: "))

if my_favorite_number == user_favorite_number:
    print("Perfect")
elif my_favorite_number < user_favorite_number:
    print("More")
else:
    print("Less")