# 3)მომხმარებელს შემოატანინე რაიმე ინდექსი 1-5 და 10 ელემენტიან სიიდან ამოიღე ამ ინდექსზე მდგომი ელემენტი და სიის დასაწყისში ჩაამატე სტრინგი "change"
my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
index = int(input("Enter an index between 1 and 5: ")) - 1
element = my_list[index]
my_list.insert(0, "change")
print(f"Element at index {index + 1}: {element}")
print(f"Updated list: {my_list}")