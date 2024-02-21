n = int(input())

def div(n):
    for i in range(1, n+1):
        if (i % 3) == 0 and (i % 4) == 0:
            yield(i)

gen = div(n)

for val in gen:
    print(val)
