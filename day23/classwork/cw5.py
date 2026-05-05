# 5)მომხმარებელს შემოატანინე მისი გვარი, შემდეგ შეეიკითხე რომელ case-ში უნდა რომ მისი გვარი დაიწეროს (თუ შემოიტანა upper, დაუბეჭდეთ მისი გვარი გადიდებულად / თუ შემოიტანა lower, დაუბეჭდეთ მისი გვარი დაპატარავებული ასოებით / თუ შემოიტანა capitalize, პირველი ასო გაადიდეთ დანარჩენი დააპატარავეთ, თუ შემოიტანა none მაშინ არ შეცვალოთ და სხვა შემთხვევაში დაუბეჭდეთ incorrect input
surname = input("შეიყვანეთ თქვენი გვარი: ")
case = input("შეიყვანეთ case (upper, lower, capitalize, none): ")
if case == "upper":
    print(surname.upper())
elif case == "lower":
    print(surname.lower())
elif case == "capitalize":
    print(surname.capitalize())
elif case == "none":
    print(surname)
else:
    print("incorrect input") 