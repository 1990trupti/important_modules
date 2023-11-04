
# import datetime
from datetime import datetime


dt_now = datetime.now()
print(dt_now)

dt_utc_now = datetime.utcnow()
print(dt_utc_now)

custom_date = datetime(2022,4,17,8,17,24,45)
custom_date = datetime(year=2019, minute=56, hour=10, day=5, month=10)
print(custom_date)


#timestamp

ts = custom_date.timestamp()
# print(ts)
# print(type(ts))
# print(dt_now.timestamp())
# print(dt_utc_now.timestamp())

dt = datetime.fromtimestamp(ts)
# print(dt)


dt_now.timestamp()
datetime.fromtimestamp(ts)
# print(dt)
# print(datetime.utcfromtimestamp(ts))

# date or time

dt = dt_now.date()
ti = dt_now.time()
# print(dt)
# print(ti)
#
# print(dt_now.day)
# print(dt_now.month)
# print(dt_now.year)
# print(dt_now.minute)
# print(dt_now.second)


combine_date = datetime.combine(dt,ti)
# print(combine_date)

replaced_date = combine_date.replace(year=2001, day=31, month=5)
# print(replaced_date)


# strptime and strftime
# strftime = datetime to string
# strptime = string to datetime


# strftime
current_datetime = datetime.now()

print(current_datetime)
print(type(current_datetime))

dt = datetime(year=2021, month=12, day=31, hour=16, minute=45)
format = "%A %Y/%m/%d %H:%M:%S"

dt_str = current_datetime.strftime(format)
dt_str = dt.strftime(format)
print(dt_str)
print(type(dt_str))

# strptime = datestr to datetime

dtstr = "Fri 31 Dec 2021 04:45 PM"
format = "%a %d %b %Y %I:%M %p"
dt = datetime.strptime(dtstr, format)
print(dt)
print(type(dt))















