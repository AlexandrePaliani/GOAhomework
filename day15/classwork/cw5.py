# 5)მომხმარებელს შემოატანინე მისი საყვარელი ფილმი და სახელი, თუ მისი სახელი ავთოა მაშინ დაპრინტე "you are avto" , თუ ლევანი ქვია და მისი საყვარელი ფილმია ტიტანიკი, დაპრინტე "Levani loves titanic" ყველა სხვა შემთხვევაში დაპრინტე "someone likes other film" 
name = input("შეიყვანეთ თქვენი სახელი: ")
favorite_movie = input("შეიყვანეთ თქვენი საყვარელი ფილმი: ")
if name == "avto":
    print("you are avto")
elif name == "levani" and favorite_movie == "titanic":
    print("Levani loves titanic")
else:
    print("someone likes other film")