import time
import datetime
now = time.gmtime(time.time())
if int(now.tm_hour) + 9  == 9 and int(now.tm_min) == 57:
    print("It's time!")
    if length("statement") == 8:
        print("wow")
else:
    print("Wait")
