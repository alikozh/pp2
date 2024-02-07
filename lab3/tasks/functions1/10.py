def unique(lst):
    for i in lst:
        if i not in uni_list:
            uni_list.append(i)


lst = list(map(int, input().split()))
uni_list = []

unique(lst)

print(uni_list)