n = int(input())

def down(n):
    i = n
    while(i>=0):
        yield (str(i))
        i-=1

gen = down(n)

lst = list(gen)

print(", ".join(lst))



    