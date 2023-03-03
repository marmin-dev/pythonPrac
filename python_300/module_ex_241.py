import datetime
print(datetime.datetime.now())
print(type(datetime.datetime.now()))

now = datetime.datetime.now()
# ex) 13:44:41
print(now.strftime("%H:%M:%S"))


ret = datetime.datetime.strptime(str(now.date()),"%Y-%m-%d")
print(now.date())
print(ret)

import time

import time
import datetime

# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)
#
import os
print(os.getcwd())

import numpy
for i in numpy.arange(0.0,5.0,0.1):
    print(i)
