# 6)შექმენით სია, შემდეგ for ციკლი დაატრიალეთ 3-ჯერ და ყოველ ჯერზე სიაში ჩაამატეთ input()
my_list = []
for _ in range(3):
    user_input = input("შეიყვანეთ რამე: ")
    my_list.append(user_input)
print(my_list)