n = int(input())

def even(n):
    i = 0
    while(i <= n):
        if i % 2 == 0:
            yield str(i)
        i += 1

l = list(even(n))
print(", ".join(l))