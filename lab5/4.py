import re

pattern = "[A-Z][a-z]+"
word = input()

print(re.findall(pattern, word))
