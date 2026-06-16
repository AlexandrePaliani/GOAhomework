# 7)შექმენით სახელების სია შემდეგ გადაუარეთ და შეამოწმეთ რომელი სახელიც იწყება "g" ასოთი დაბეჭდეთ ეს სახელი და გვერდით მიუწერეთ True
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]
for name in names:
    if name.startswith("G"):
        print(name, True)