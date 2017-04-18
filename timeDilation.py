
import numpy as np
import matplotlib.pyplot as plt
import csv
from tzwhere import tzwhere
from scipy.optimize import minimize_scalar
from scipy.optimize import fsolve
from scipy.integrate import odeint

csvdata = list(csv.reader(open("UTFData.csv")))
csvdata = np.array(csvdata)
dataset1=[[36.6,-121.89846],[52.1427,6.1961],[-37.8136,144.9631],[31.2304,121.4737],[22.39,114.1095],[55.7558,37.6173]]
dataset2=[[42.3601,-71.0589],[42.3601,-71.0589],[1.3521,103.8198],[39.91,160.3636],[22.3964,114.1095],[22.3964,114.1095],[55.7558,37.6173],[52.0907,5.1412],[52.2297,21.0122],[55.6761,12.5683],[-37.8136,144.9631]]
latlongarray=dataset2

tz = tzwhere.tzwhere()

panic = False

def longToTzName(lat,long):
    return tz.tzNameAt(lat,long)

def longToTz(name):
    panic=False
    i=0
    if (name == None):
        panic = True
        return 0
    else:
        while(i<(csvdata.shape[0])):
            if(csvdata[i][2]==name):
                return csvdata[i][4]
            else:
                i+=1
        i=0
    
def timeDilation(TZa,TZb):
    print(TZa,TZb)
    diff1=np.float(TZb)-np.float(TZa)
    if (diff1==0):
        return 0
    else:
        diff2=(-diff1/abs(diff1))*(24-abs(diff1))
        if (abs(diff2)<abs(diff1)):
            return diff2
        elif (abs(diff2)>abs(diff1)):
            return diff1
        elif (abs(diff2)==abs(diff1)):
            return diff2

def difference(latlongarray,k,loc):
    x = longToTz(longToTzName(latlongarray[k][0],latlongarray[k][1]))
   # y= longToTz(longToTzName(loc[0],loc[1]))
    #print('x,y:',x,y)
    return timeDilation(x,loc)
    


def kuramoto(rinit,t,omega,delta,k,f):
    x, y = rinit
    drdt = [0.5*(k*x+f-k*x**3-f*x**2+k*x*y**2+f*y**2-2*k*x*y**2)-delta*x+omega*y, 0.5*(k*y+k*y*x**2-k*y**3-2*k*y*x**2-2*f*x*y)-delta*y-omega*x]
    return drdt

#parameters
delta =.0038
k = 4.5*delta
f = 3.5*delta
omega = 2*np.pi*(1/24-1/24.5)

equilguess=[.79766,-.34587]
t = np.linspace(0,350, 10000)
equil = fsolve(kuramoto,equilguess,args=(t,omega,delta,k,f))
def jetlaginit(deltap):
    return [equil[0]*np.cos(deltap*np.pi/12)+equil[1]*np.sin(deltap*np.pi/12),-equil[0]*np.sin(deltap*np.pi/12)+equil[1]*np.cos(deltap*np.pi/12)] 

options=()    

def cost(latlongarray,loc):
    panic=False
    cost=np.zeros(10000)
    for k in range(len(latlongarray)):
        if (panic == True):
            return 1000000
            panic = False
        else:
            temp=difference(latlongarray,k,loc)
            deltap=temp
            sol=odeint(kuramoto,jetlaginit(deltap),t,args=(omega,delta,k,f))
            sollag=np.sqrt((sol[:,0]-equil[0])**2+(sol[:,1]-equil[1])**2)
            cost=cost+sollag
        
    return cost
def constraint(x):
    return (4*x[0])%2
cons=[{'type':'eq','fun':constraint}]
def thingtominimize(x):
   tempcosttotal=0
   # return SUM OF FIRST HOWEVER MANY (cost(latlongarray[x,y]))
   tempcost=cost(latlongarray,x[0])
   for j in range(0,2057):
      tempcosttotal=tempcosttotal+tempcost[j]   
   return tempcosttotal

#print(minimize(thingtominimize,np.array([8.5]),method="SLSQP",constraints=cons,options={'disp':True,'ftol':1e-15}))

i=0
correctzone=0
totalcost=10000000000000000000000000000
k=0
while i<24:
    cost=0
    temptotalcost=0
    print('i;',i)
    for k in range(len(latlongarray)):
        deltap = i - int(longToTz(longToTzName(latlongarray[k][0],latlongarray[k][1])))
        sol=odeint(kuramoto,jetlaginit(deltap),t,args=(omega,delta,k,f))
        sollag=np.sqrt((sol[:,0]-equil[0])**2+(sol[:,1]-equil[1])**2)
        cost=cost+sollag
        if (panic == True):
            cost=10000000000
            panic = False
    for j in range(0,2057):
        temptotalcost=temptotalcost+cost[j]
    if (temptotalcost<totalcost):
        totalcost=temptotalcost
        correctzone=i
    print(temptotalcost)
    i=i+1
print(correctzone,totalcost)



#print(minimize(testfunc,np.array([5,5]),method='Powell',options={'maxiter':20,'disp':True}))
#print(minimize(thingtominimize,np.array([39.0392,125.7625]),method="Powell",options={'maxiter':1 , 'disp':True}))

#plt.plot(t, np.sqrt((sol[:,0]-equil[0])**2+(sol[:,1]-equil[1])**2), label=deltap)
    

#plt.legend(loc='best')


