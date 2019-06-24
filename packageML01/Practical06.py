import datetime

n = datetime.datetime.now()
print("now = ", n)

print(n.year, n.month, n.day, n.hour, n.minute, n.second, n.microsecond)

print(n.strftime("%B"))
print(n.strftime("%b"))