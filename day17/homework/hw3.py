
# 3)შექმენით სია სადაც იქნება 10 რიცხვი და შექმენით sum ცვლადი რომლის საშუალებითაც გამოითვლით ამ ყველა რიცხვის ჯამს.
numbers = [4, 15, 23, 8, 42, 16, 7, 9, 30, 11]
total_sum = 0
for num in numbers:
    total_sum += num
print(f"Total sum: {total_sum}")