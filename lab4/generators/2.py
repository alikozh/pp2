n = int(input())

def even(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield(str(i))

gen = even(n)
lst = list(gen)

print(lst)
print(", ".join(lst))


    