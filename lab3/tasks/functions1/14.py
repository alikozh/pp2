from itertools import permutations
def perm(str):
    res = permutations(str)
    for i in res:
        print(''.join(i))
    
perm(str(input()))


def solve(numheads, numlegs):
    y = numlegs/2 - numheads
    print("Chickens:", numheads - y, "Rabbits:", y)

numheads = int(input("heads:"))
numlegs = int(input("legs:"))

solve(numheads, numlegs) 