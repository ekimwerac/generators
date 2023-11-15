def count_up_to(limit):
    count = 0
    while count < limit:
        yield count
        count += 1

# Create a generator object
my_generator = count_up_to(5)

# Use next() to retrieve values from the generator
print(next(my_generator))  # Output: 0
print(next(my_generator))  # Output: 1
print(next(my_generator))  # Output: 2
print(next(my_generator))  # Output: 3
print(next(my_generator))  # Output: 4

# If you try to call next() beyond the available values, it raises StopIteration
try:
    print(next(my_generator))  # Raises StopIteration
except StopIteration:
    print("Generator is exhausted.")
