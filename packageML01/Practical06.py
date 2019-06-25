import datetime as dt

now = dt.datetime.now()
print("\nNow:- ",now)

print(now.year , now.month , now.day , now.hour , now.minute , now.second , now.microsecond)

print(now.strftime("%B"))
print(now.strftime("%b"))