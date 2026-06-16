# 2)შექმენით .split()-ის კლონი.
def custom_split(string, delimiter):
    result = []
    current_word = ""
    for char in string:
        if char == delimiter:
            result.append(current_word)
            current_word = ""
        else:
            current_word += char
    result.append(current_word)  # Add the last word
    return result