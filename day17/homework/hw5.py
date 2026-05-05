# 5) for ციკლით გადაუარე სიას და დაბეჭდე მხოლოდ ის ელემენტები, რომელთა ინდექსი ლუწია.
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
for index in range(len(my_list)):
    if index % 2 == 0:
        print(my_list[index])  