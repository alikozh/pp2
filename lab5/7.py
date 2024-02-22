import re

text = "snake_case_example_string" #snakeCaseExampleString

snake = re.split(r"_", text)

print(snake)
print(len(snake))

s = snake[0]
for i in range(1, len(snake)):
    s += snake[i].capitalize()

print(s)

