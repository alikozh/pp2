def check_palind(num):
    temp = str(num)
    return temp == temp[::-1]

def gen_palind(start, stop):
    while start < stop:
        if check_palind(start):
            yield (start)
            
        start += 1

pal = list(gen_palind(1, 1000))

print(pal)