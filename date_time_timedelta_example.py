from datetime import date,time,timedelta,datetime


today = date.today()
print(today)

dt = date(2023,2,2)
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)

print(date.max)
print(date.min)

new_dt = dt.replace(2021,3,3)
print(type(new_dt))

print(today.weekday())    #monday to sunday
print(today.isoweekday())   #sunday to monday


print(dt.strftime("%Y/%d/%m"))

#time

x = time(10,10,10)
print(x)
print(x.strftime("%H:%M:%S"))

print(x.replace(hour=15))


# timedelta

td = timedelta(hours=1,minutes=5,seconds=45,microseconds=60)

dt1 = datetime(2023,4,17,10)
dt2 = datetime(2023,4,17,9)

print(dt1+td)
print(dt2+td)

print(type(dt1-dt2))

exp = datetime(2023,4,18)

# token = datetime.now()
# valid_dt = datetime.now() + timedelta(seconds=2)
# print(valid_dt)

# while True:
#     print("1")
#     if datetime.now() > valid_dt:
#         break

# if datetime.now() >=exp:
#     print("expired")


token_expiry = datetime.now() + timedelta(seconds=3)

def request_to_sbi():
    if datetime.now() <= token_expiry:
        return "allowed"
    return "not allowed"

print(request_to_sbi())
import time
time.sleep(4)
print(request_to_sbi())












