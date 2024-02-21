import datetime

now = datetime.datetime.now()

print(f"Yesterday: {now - datetime.timedelta(1)}")

print(f"Today: {now}")

print(f"Yesterday: {now + datetime.timedelta(days = 1)}")
