# 7)შექმენით sum ფუნქციის იდენტური ვარიანტი (sum ფუნქციას გადაეცემა ინტეჯერების სია და გამოაქ ამ ინტეჯერების ჯამი)
def my_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total