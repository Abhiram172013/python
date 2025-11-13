import random 
import time 
def getrandomdate(startdate,enddate):
    print("printing random date between",startdate,enddate)
    randomgenerator=random.random()
    dateFormat="%m/%d/%y"
    starttime=time.mktime(time.strptime(startdate,dateFormat))
    endtime=time.mktime(time.strptime(enddate,dateFormat))
    randomtime=starttime+randomgenerator*(endtime-starttime)
    randomdate=time.strftime(dateFormat,time.localtime(randomtime))
    return randomdate
print("randomdate=",getrandomdate("1/1/25","12/12/25"))
