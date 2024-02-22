import re

pattern = r"[ ,.]"

text = "for instance, i don't have this one."

res = re.sub(pattern, ":", text)
print(res)