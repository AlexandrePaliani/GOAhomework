# 
# 5)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგი და ინტეჯერი, ასევე ფუნქციას ქონდეს სია რომელშიც ჩაამატებ მომხმარებლის შემოტანილ სტრინგს იმ ინდექსზე რომელიც მან შემოიტანა
def insert_string_at_index(s, index, lst):
    if index < 0 or index > len(lst):
        print("Invalid index")
        return lst
    lst.insert(index, s)
    return lst  
