# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:58:38 2017

@author: avata
"""

import numpy as np
import csv
from tzwhere import tzwhere

csvdata = list(csv.reader(open("UTFData.csv")))
csvdata = np.array(csvdata)


tz = tzwhere.tzwhere()

def longToTzName(lat,long):
   return tz.tzNameAt(lat,long)

def longToTz(name):
    i=0
    while(i<(csvdata.shape[0])):
        if(csvdata[i][2]==name):
            return csvdata[i][4]
            print(i)
        else:
            i+=1
            print(i)
    i=0
    
def timeDilation(TZa,TZb):
    diff1=TZb.astype(np.float)-TZa.astype(np.float)
    diff2=(-diff1/abs(diff1))*(24-abs(diff1))
    if (abs(diff2)<abs(diff1)):
        return diff2
    elif (abs(diff2)>abs(diff1)):
        return diff1
    elif (abs(diff2)==abs(diff1)):
        return diff2
    
#print(longToTz(longToTzName(40,-75)))
#print(pytz.timezone("America/Los_Angeles"))
print(timeDilation(longToTz(longToTzName(16.7666,-3.0026)),longToTz(longToTzName(35.6895,139.6917))))
