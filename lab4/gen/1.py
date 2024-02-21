def myRange(start, stop):
    while start < stop:
        yield start
        start += 1

gen = myRange(1, 20)
nums = list(gen)

print(', '.join(map(str, nums)))