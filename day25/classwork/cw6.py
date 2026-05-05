# 
# 6)შექმენით len ფუნქციის იდენტური ვარიანტი
def my_len(lst):
    count = 0
    for _ in lst:
        count += 1
    return count