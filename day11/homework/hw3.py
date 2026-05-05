# 3)მომხმარებელს შემოატანინეთ მისი სახელი, შემოატანინეთ მისი ასაკი, ასევე სიმაღლე და შეამოწმეთ თუ მომხმარებლის ასაკი მეტია 18 და მისი სახელი უდრის თქვენს სახელს და ასევე მისი სიმაღლე მეტია 1.80-ზე

name = input("enter your name here: ")
age = int(input("enter your age here: "))
size = float(input("enter your height here:"))

print(name == "alex" and age > 18 and size > 1.80)