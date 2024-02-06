def filter_prime(lst):
    for i in lst:
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count+=1
        
        if count == 2:
            prime_lst.append(i)


lst = list(map(int, input().split()))
prime_lst = []

filter_prime(lst)

print(prime_lst)

for i in prime_lst:
    print(i)