#generator
def generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
for value in generator():
    print(value)
    # Output:
    # 1
    # 2
    # 3
    # The generator function produces a sequence of values, and the for loop iterates over those values, printing each one.
    # The yield statement allows the function to return a value and pause its execution, resuming from the same point when the next value is requested.
    # This makes generators memory-efficient, as they generate values on-the-fly rather than storing the entire sequence in memory at once.
    # In this example, the generator produces the values 1, 2, and 3, which are printed one by one in the loop.
    # You can also use the next() function to manually retrieve values from the generator:
gen = generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
