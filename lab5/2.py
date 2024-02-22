import re

pattern = r"ab{2,3}"

word = input()

print(re.findall(pattern, word))