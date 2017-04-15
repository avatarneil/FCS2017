import numpy as np
import matplotlib.pyplot as plt
carray = []
c2array = []
tarray = []
harray = []
sumhcarray = []

def eulers():
    dt = 0.1 # hr
    t=0
    i=0
    c=0
    mu = .3
    c2=-1
    hasy=4
    h0=1
    t0=16
    xs=3
    xw=18
    thresh=3
    sleepstatus=1
    h=0
    omega=(2*np.pi)/24
    u=.01
    
    while t<=120:
        dcdt = mu*(c*omega**2-(1/3)*c**3-c2)
        dc2dt = ((1/mu)*c)*omega**2
        c=c+dcdt*dt
        c2=c2+dc2dt*dt
        c=c*np.e**(-h*u)
        if (h-c>=thresh and sleepstatus==1):
            sleepstatus=0
            print(t,sleepstatus)
        elif(np.abs(h-c)<.1 and sleepstatus==0):
            sleepstatus=1
            print(t,sleepstatus)
        
        if(sleepstatus==1):
            dhdt=(-h/xw)+(hasy/xw)
        else:
            dhdt=(-h/xs)
            
        h=h+dhdt*dt
        
        harray.append(h)    
        carray.append(c)
        c2array.append(c2)
        tarray.append(t)
        sumhcarray.append(h+c)
        t=t+dt
        i=i+1
        
eulers()
#plt.plot(tarray,sumhcarray,'purple',label='hc')
plt.plot(tarray,carray,'r',label='C')
plt.plot(tarray,harray,'g',label='h')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.savefig("test.svg")
#call function