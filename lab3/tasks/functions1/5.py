from itertools import permutations
def perm(str):
    res = permutations(str)
    for i in res:
        print(''.join(i))
    
perm(str(input()))