# 2)მომხმარებელს შემოატანინე რაიმე ცხოველები და ჩასვი ისინი სეტში, შემდეგ მთლიანად გაასუფთავე ეს სეტი
animals = set()
while True:
    animal = input("შეიყვანეთ ცხოველი (გასასუფთავებლად ჩაწერეთ 'გასუფთავება'): ")
    if animal.lower() == "გასუფთავება":
        break
    animals.add(animal)
animals.clear()
print(animals)