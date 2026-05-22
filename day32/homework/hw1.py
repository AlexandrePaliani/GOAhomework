# 1)შექმენით .join()-ის კლონი.
def my_join(separator, iterable):
    result = ""
    for i, item in enumerate(iterable):
        result += str(item)
        if i < len(iterable) - 1:
            result += separator
    return result