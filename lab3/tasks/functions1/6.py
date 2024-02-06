"""""
def rev(string):
    print(string[::-1])

rev(input())

"""""

sent = list(input().split())

def rev(a):
    res = a[::-1]
    fin = ' '.join(map(str, res))
    print(fin)

rev(sent)