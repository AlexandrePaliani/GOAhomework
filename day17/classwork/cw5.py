# 5)შექმენით სახელების სია და მომხმარებლებს შემოატანინეთ მისი სახელი ასევე count ცვლადი, გადაუარეთ ამ სიას და რამდენჯერაც მომხმარებლის სახელი შეგხვდებათ დაპრინტე "user name" და count მოუმატე ერთი საბოლოოდ  დაპრინტე count ცვლადი

names = ["Alice", "Bob", "Charlie", "Alice", "David"]
user_name = input("Enter a user name: ")
count = 0

for name in names:
    if name == user_name:
        print("user name")
        count += 1

print(count)