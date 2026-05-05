# 5) დაწერე ფუნქცია რომელიც იღებს სიტყვების სიას და აბრუნებს ყველაზე გრძელ სიტყვას.
def get_longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest