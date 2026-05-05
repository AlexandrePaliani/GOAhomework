# 6) შექმენით ინტეჯერების ლისტი, და ორი ცვლადი positive, negative. გამოიტანეთ სიაში არსებული დადებითი რიცხცების ჯამი, უარყოფითები რიცხვების რაოდენობა და დაპრინტე "zero" რამდენჯერაც შეგხვდება 0
numbers = [1, -2, 3, 0, -5, 6, 0, -1, 4, 0]
positive_sum = 0
negative_count = 0
zero_count = 0

for num in numbers:
    if num > 0:
        positive_sum += num
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f"Sum of positive numbers: {positive_sum}")
print(f"Count of negative numbers: {negative_count}")
print(f"Count of zeros: {zero_count}")