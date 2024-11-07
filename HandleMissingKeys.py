# Avoid KeyError by using get() when accessing dictionary values. This is especially useful when you’re not sure if a key exists.

person = {"name": "Alice", "age": 25}
print(person.get("name"))  # Output: Alice
print(person.get("gender", "Not specified"))  # Output: Not specified
