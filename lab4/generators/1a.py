n = int(input())

def square(n):
    i = 1
    while(i**2 <= n):
        print(i * i)
        i+=1

square(n)

print("----")

def squ(n):
    i = 1
    while(i**2 <= n):
        yield(i**2)
        i+=1

gen = squ(n)

for i in gen:
    print(i)
