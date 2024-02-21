import datetime

date1 = datetime.date(2024, 2, 12)
date2 = datetime.date(2024, 1, 31)

delta = date1 - date2

print(delta)
print(delta.total_seconds())


#ex5

from datetime import datetime

time = datetime.now().time()
print(time)