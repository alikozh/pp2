import re

text = input()

print(re.sub(r"([a-z])([A-Z])", "\\1_\\2", text).lower())