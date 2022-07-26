import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(type(now))

date_of_birth = dt.datetime(year=1998, month=8, day=31)
print(date_of_birth)
