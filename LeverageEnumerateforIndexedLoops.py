# When you need both the index and the value in a loop, enumerate() can simplify your code.

# Without enumerate
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i, fruits[i])

# With enumerate
for i, fruit in enumerate(fruits):
    print(i, fruit)
