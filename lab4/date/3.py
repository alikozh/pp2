import datetime 

now = datetime.datetime.now()

without_microsec = now.replace(microsecond=0)

print(f"time without microseconds: {now.replace(microsecond=0)}")

print(without_microsec)

