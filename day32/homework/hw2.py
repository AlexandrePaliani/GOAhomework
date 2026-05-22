# 
# 2)შექმენით .split()-ის კლონი.
def my_split(separator, string):
    result = []
    current_word = ""
    for char in string:
        if char == separator:
            result.append(current_word)
            current_word = ""
        else:
            current_word += char
    result.append(current_word)  # Add the last word
    return result