# 2)შექმენით სია შემდგარი 7 განსხვავებული ემენეტისგან და for ციკლის მეშვეობით შეამოწმეთ თითოეული ემენეტის მონაცემთა ტიპი
mixed_list = [1, "hello", 3.14, True, [1, 2], {"key": "value"}, None]
for item in mixed_list:
    print(f"Element: {item}, Type: {type(item)}")
    
