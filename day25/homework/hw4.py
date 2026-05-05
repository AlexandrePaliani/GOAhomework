# 4)დაწერე ფუნქცია, რომელიც დააბრუნებს მხოლოდ ლუწ რიცხვებს ახალი list-ის სახით
def get_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]