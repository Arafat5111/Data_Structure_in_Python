fruits = {"Banana", "Apple", "Mango", 200}
print(fruits)
fruits.remove(200)
print(fruits)
fruits.remove("Banana")
print(fruits)
fruits.discard("Apple")
fruits.discard("Hello") #if it exisst then it will be rmove otherwise it is do not trough error
print(fruits)