import re

pochta = input()
pattern1 = "@mail.ru"
pattern2 = "@gmail.com"


if re.findall(pattern1, pochta) == ["@mail.ru"] or re.findall(pattern2, pochta) == ["@gmail.com"] :
    print("pochta is valid")

else:
    print("pochta is not valid")
