# When you need to loop over multiple lists at once, zip() is a quick and readable solution.

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")
