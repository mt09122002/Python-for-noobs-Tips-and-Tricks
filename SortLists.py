# Python makes it easy to sort lists with either sorted() (which returns a new sorted list) or list.sort() (which sorts in place).

numbers = [3, 1, 4, 1, 5, 9]
sorted_numbers = sorted(numbers)  # [1, 1, 3, 4, 5, 9]
numbers.sort()  # [1, 1, 3, 4, 5, 9]
