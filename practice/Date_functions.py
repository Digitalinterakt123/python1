import time,calendar;

localtime = time.localtime(time.time())
localtime1 = time.asctime( time.localtime(time.time()) )
localtime12 = time.clock()
print("Local current time :", localtime12)

# cal = calendar.month(2008, 8)
# print("Here is the calendar:")
# print (cal)