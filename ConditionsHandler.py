# These functions simplify checks on lists or other iterables. 
# any() returns True if any element is True, while all() returns True only if all elements are True.

numbers = [0, 1, 2, 3]
print(any(numbers))  # True (since at least one number is non-zero)
print(all(numbers))  # False (since 0 is in the list)
