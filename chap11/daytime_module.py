import datetime

mytime = datetime.time(2,20)
print(mytime)
print(mytime.hour)
today = datetime.date.today()
print(today)
from datetime import datetime
today.replace(year=2022)
print(today)
from datetime import date
date1 = date(2015,11,21)
date2 = date(2023,2,20)

print(date2 - date1)