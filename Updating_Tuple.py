fruits = ("Banna", "Apple", "Mango", ["arafat", 100], 200)

fruits = list(fruits)
fruits[1] = "Pinapple"
fruits = tuple(fruits)
print(fruits)

fruits = list(fruits)
fruits.append(20)
fruits.append(2)
fruits.append(25)
fruits = tuple(fruits)
print(fruits)

fruits = list(fruits)
fruits.remove(200)
fruits.remove(fruits[1])
fruits = tuple(fruits)
print(fruits)