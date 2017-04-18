from GeoBases import GeoBase
import numpy as np
import matplotlib.pyplot as plt
import csv
from tzwhere import tzwhere
import scipy.optimize as sp
from scipy.integrate import odeint

geo_a = GeoBase(data='airports',verbose=False)

csvdata = list(csv.reader(open("UTFData.csv",encoding='utf-8')))
csvdata = np.array(csvdata)
dataset1=[[36.6,-121.89846],[52.1427,6.1961],[-37.8136,144.9631],[31.2304,121.4737],[22.39,114.1095],[55.7558,37.6173]]
dataset2=[[42.3601,-71.0589],[42.3601,-71.0589],[1.3521,103.8198],[39.91,160.3636],[22.3964,114.1095],[22.3964,114.1095],[55.7558,37.6173],[52.0907,5.1412],[52.2297,21.0122],[55.6761,12.5683],[-37.8136,144.9631]]
latlongarray=dataset1
#conference=[59.9343,30.3351]
#conference=[24.958202,46.700779]
#conference=[-11.2027,17.8739]

tz = tzwhere.tzwhere()

panic = False
if (latlongarray==dataset1):
    zonerestriction=3
elif (latlongarray==dataset2):
    zonerestriction=1
#loc1 = (37.5665,126.9780)
#loc2 = (59.9139,10.7522)

def price(loc1,loc2):
    airport1 = list(geo_a.findClosestFromPoint(loc1))
    airport2 = list(geo_a.findClosestFromPoint(loc2))
    distance = (geo_a.distance(airport1[0][1],airport2[0][1]) * .621371)
    #print(distance)
    if (geo_a.get(airport1[0][1],'country_code') == geo_a.get(airport2[0][1],'country_code')):
        if(distance<=1):
            price = 0
        else:
            price = (.032 * (distance*2)) + 230
    else:
        price = (.08 * (distance*2)) + 200
    return price
#print(price((latlongarray[0][0],latlongarray[0][1]),(conference[0],conference[1])))

def longToTzName(lat,long):
    return tz.tzNameAt(lat,long)

def longToTz(name):
    panic=False
    i=0
    if (name is None):
        panic = True
        return 0
    else:
        while(i<(csvdata.shape[0])):
            if(csvdata[i][2]==name):
                return csvdata[i][4]
            else:
                i+=1
        i=0

def flightcost(x):
    tempprice=0
    if (float(longToTz(longToTzName(x[0],x[1]))) - zonerestriction == 0):
        for i in range (len(latlongarray)):
            tempprice = tempprice + price((latlongarray[i][0],latlongarray[i][1]),(x[0],x[1]))
        print(tempprice)
        return tempprice
    else:
        return 100000000000

def utcconstraint(x):
    return int(longToTz(longToTzName(x[0],x[1]))) - zonerestriction

locationconstraints = [{'type':'eq','fun':utcconstraint}]

print(sp.brute(flightcost,[(0,62),(25,50)],Ns=186,disp=True))
#print(longToTz(longToTzName(58.9,16.57894737)))
#print(list(geo_a.findClosestFromPoint((58.64864865,52.32972973))))

