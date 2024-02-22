import re

pattern1 = r"Стоимость"

def match(pattern):
    with open("row.txt", "r", encoding="utf-8") as file:
        text = file.read()
        matches = re.findall(pattern, text)

    return matches

print(match(pattern1))
