# 3)შექმენით ცვლადი name და age, თუ სახელი უდრის გიორგის და 18 წელზე მეტისაა დაპრინტოს adult giorgi, თუ 18 წელზე ნაკლებისაა დაპრინტოს "not adult giorgi", და თუ საერთოდ არ ქვია გიორგი დაპრინტოს 'not giorgi" (indented if-else)
name = input("შეიყვანეთ თქვენი სახელი: ")
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
if name == "giorgi":
    if age > 18:
        print("adult giorgi")
    else:
        print("not adult giorgi")
else:
    print("not giorgi")