import re

pattern = r"[a-z]+_[a-z]+"
word = input()

print(re.findall(pattern, word))