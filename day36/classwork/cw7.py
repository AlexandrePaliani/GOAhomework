# 6) შექმენი ორი სეტი და გამოიტანე ელემენტები რომელიც ერთ სეტში არის და მეორეში არა
set1 = {"ა", "ბ", "გ", "დ"}
set2 = {"გ", "დ", "ე", "ვ"}
unique_to_set1 = set1.difference(set2)
unique_to_set2 = set2.difference(set1)
print(unique_to_set1)
print(unique_to_set2)

# 7)წინა დავალებაში შექმნილი ორი სეტიდან გამოიტანე ელემენტები რომლებიც უნიკალურია (ერთერთში თუ არის მაშინ მეორეში აღარ უნდა იყოს)
unique_to_set1 = set1.difference(set2)
unique_to_set2 = set2.difference(set1)
print(unique_to_set1)
print(unique_to_set2)