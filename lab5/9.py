import re

text = input()

print(re.sub(r"([A-Z])", " \\1", text))

