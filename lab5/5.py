import re

pattern = r"a.*\Bb"
word = input()

print(re.findall(pattern, word))
