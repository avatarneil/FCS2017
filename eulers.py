import numpy as np
import matplotlib.pyplot as plt
carray = []
cdarray=[]
c2array = []
c2darray=[]
tarray = []
harray = []
hdarray=[]
alertarray = []
alertdarray=[]
wakesleeparray=[]
wakesleepdarray=[]
def eulers():
    dt = 0.1 # hr
    t=0
    i=0
    c=0
    
    mu = .3
    c2=-1
    c2d=-1
    hasy=15
    h0=1
    t0=16
    xs=3
    xw=18
    threshinit=7
    thresh=threshinit
    sleepstatus=1
    dsleepstatus=1
    h=0
    hd=0
    omega=(2*np.pi)/24
    u=.01
    o=5
    A=1
    phi=0
    cd=0
    sleepfreedom=0
    while t<=72:
        thresh=thresh+np.random.randn()
        
        #C euler function
        dcdt = mu*(c-(1/3)*c**3-c2)
        dcddt = mu*(cd-(1/3)*cd**3-c2d)
        dc2dt = (1/mu)*(c*omega**2-A*np.sin(omega*t))
        dc2ddt = (1/mu)*(cd*omega**2-A*np.sin(omega*t+phi))
        c=c+dcdt*dt
        cd = cd +dcddt*dt
        c2=c2+dc2dt*dt
        c2d = c2d+dc2ddt*dt
        #enable/disable sleep
        if ((0<=t and t<=8)) or ((24<=t and t<=32)) or (48<=t and t<=56):
            sleepfreedom=0
        else:
            sleepfreedom=1
        print(sleepfreedom,t)
        if (sleepfreedom==0):
            sleepstatus=1
            dsleepstatus=1
        if (sleepfreedom==1):
            if ((h-c)>=thresh and sleepstatus==1):
                sleepstatus=0
            elif(np.abs(h-c)<.2 and sleepstatus==0):
                sleepstatus=1
            if ((hd-cd)>=thresh and dsleepstatus==1):
                dsleepstatus=0
            elif(np.abs(hd-cd)<.2 and dsleepstatus==0):
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
        hdarray.append(hd)
        carray.append(c)
        cdarray.append(cd)
        c2array.append(c2)
        c2darray.append(c2d)
        tarray.append(t)
        if (sleepstatus==1):
            alertarray.append(h-c)
        elif (sleepstatus==0):
            alertarray.append(c+h)
        if (dsleepstatus==1):
            alertdarray.append(hd-cd)
        elif (dsleepstatus==0):
            alertdarray.append(cd+hd)
        t=t+dt
        i=i+1
        thresh=threshinit

eulers()
#plt.plot(tarray,alertarray,'purple',label='hc')
plt.plot(tarray,alertdarray,'green',label='driven hc')
#plt.plot(tarray,wakesleeparray,'r',label='wakesleep')
plt.plot(tarray,wakesleepdarray,'b',label='wakesleepd')
#plt.plot(tarray,carray,'r',label='C')
#plt.plot(tarray,cdarray)
#plt.plot(tarray,hdarray)
#plt.plot(tarray,harray,'g',label='h')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.savefig("test.svg")
#call function