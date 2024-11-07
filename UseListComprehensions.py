# List comprehensions provide a more concise way to create lists. 
# They can replace loops and append() calls, making code shorter and often faster.

# Traditional way
squares = []
for i in range(10):
    squares.append(i * i)

# Using list comprehension
squares = [i * i for i in range(10)]

