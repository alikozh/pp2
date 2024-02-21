n = int(input())

def square(n):
    i = 1
    while i**2 <= n:
        yield i**2
        i += 1

for i in square(n):
    print(i)
