# 1)შექმენით .join()-ის კლონი.
def custom_join(separator, iterable):
    result = ""
    for i, item in enumerate(iterable):
        if i > 0:
            result += separator
        result += str(item)
    return result