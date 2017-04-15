import numpy as np
import matplotlib.pyplot as plt
carray = []
cdarray=[]
c2array = []
c2darray=[]
tarray = []
harray = []
alertarray = []
alertdarray=[]
wakesleeparray=[]
wakesleepdarray=[]
def eulers():
    dt = 0.1 # hr
    t=0
    i=0
    c=0
    cd=0
    mu = .3
    c2=-1
    c2d=0
    hasy=6
    h0=1
    t0=16
    xs=3
    xw=18
    thresh=3
    sleepstatus=0
    dsleepstatus=1
    h=0
    hd=0
    omega=(2*np.pi)/24
    u=.01
    o=5
    A=0.25
    phi=5
    while t<=36:
        thresh=thresh+np.random.randn()
        
        #C euler function
        dcdt = mu*(c-(1/3)*c**3-c2)
        dcddt = mu*(cd-(1/3)*cd**3-c2d)
        dc2dt = (1/mu)*(c*omega**2)
        dc2ddt = (1/mu)*(cd*omega**2-A*np.sin(omega*t+phi))
        c=c+dcdt*dt
        cd = cd +dcddt*dt
        c2=c2+dc2dt*dt
        c2d = c2d+dc2ddt*dt
        #enable/disable sleep
        if (h-c>=thresh and sleepstatus==1):
            sleepstatus=0
        elif(np.abs(h-c)<.1 and sleepstatus==0):
            sleepstatus=1
        if (h-cd>=thresh and dsleepstatus==1):
            dsleepstatus=0
        elif(np.abs(h-cd)<.1 and dsleepstatus==0):
            dsleepstatus=1
        
        #H euler function
        if(sleepstatus==1):
            dhdt=(-h/xw)+(hasy/xw)
            wakesleeparray.append(10)
        else:
            dhdt=(-h/xs)
            wakesleeparray.append(5)
        h=h+dhdt*dt
        
        if(dsleepstatus==1):
            dhddt=(-hd/xw)+(hasy/xw)
            wakesleepdarray.append(9)
        else:
            dhddt=(-hd/xs)
            wakesleepdarray.append(4)
        hd=hd+dhddt*dt
        
        #append arrays
        harray.append(h)    
        carray.append(c)
        cdarray.append(cd)
        c2array.append(c2)
        c2darray.append(c2d)
        tarray.append(t)
        alertarray.append((c+h))
        alertdarray.append((cd+hd))
        t=t+dt
        i=i+1
        thresh=3

eulers()
#plt.plot(tarray,alertarray,'purple',label='hc')
plt.plot(tarray,alertdarray,'green',label='driven hc')
#plt.plot(tarray,wakesleeparray,'r',label='wakesleep')
plt.plot(tarray,wakesleepdarray,'b',label='wakesleepd')
#plt.plot(tarray,carray,'r',label='C')
#plt.plot(tarray,cdarray)
#plt.plot(tarray,harray,'g',label='h')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.savefig("test.svg")
#call function