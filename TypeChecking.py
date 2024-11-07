# When you need to check the type of a variable, use isinstance() for readability and flexibility.

def process_data(data):
    if isinstance(data, list):
        print("Processing list...")
    elif isinstance(data, dict):
        print("Processing dictionary...")

process_data([1, 2, 3])  # Output: Processing list...

