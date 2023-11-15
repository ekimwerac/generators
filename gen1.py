def square_generator(n):
    for i in range(n):
        yield i * i

# Using the generator in a for loop
for result in square_generator(5):
    print(result)
