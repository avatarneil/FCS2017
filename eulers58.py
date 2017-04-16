import numpy as np
import matplotlib.pyplot as plt
carray = []
c2array = []
tarray = []
harray = []
wakesleeparray=[]
cogtarray = []
CCarray = []
warray = []
intensityarray=[]
barray=[]
darray=[]
d2array=[]

def intensity(z):
    return 5000
    
        

def eulers():
    dt = .01
    t = 0
    sleepstatus = 0
    twake = 8 #when subject woke up 
    
    #C constants -- There will be a million of them
    mu = .13
    q = (1/3)
    tx = 24.2
    k = .55
    beta = .013
    G = 19.875 
    alpha0 = .16
    p=.6
    xmin = 8
    
    #H constants
    rhsl = (1/2.14)
    uh = .95
    rhw = (1/38)
    uc = .1503
    
    #CC constants
    a = 9.27*10**(-6)
    hac = .098
    
    #W constants
    w0 = -.2868
    w=w0
    rw = (1/.86)
    
    #initial conditions
    c = -1.1
    c2 = -1.22
    d = -1.1
    d2 = -1.22
    n = .5
    h = .85
    
    #coupling constants
    fcd=0
    fdc=.1
    
    
    cbtmin = xmin + .8
    while t<=100:
        #C euler function
        
        #sleepwakecycle
        if ((t%24)>=0 and (t%24)<8):
            sleepstatus = 0
        elif (((t%24)-8) <=0.01):
            sleepstatus = 1
            twake=t
        else:
            sleepstatus=sleepstatus
        
        #alpha&n -- Light stuff
        I = intensity(t)
        alpha = alpha0*(I/9500)**p
        dndt = 60*(alpha*(1-n)-beta*n)
        
        #b -- Driving function caused by light
        b = (G * (1-n) * alpha * (1-.4*d) * (1-.4*d2))
        #b=(1-c/3) * .018 * I**(1/3)
        #C stuff
        
        dcdt = (np.pi/12) * (c2 + mu*(c/3+(4*c**3)/3-(256*c**7)/105))
        dddt = (np.pi/12) * (d2 + mu*(d/3 +(4*d**3)/3-(256*d**7)/105) + b)
        #we need to increase frequency of the 2nd ocillator
        dc2dt = (np.pi/12) * (-c*((24/(tx*.99729))**2)) + (1/mu)*fdc*dddt
        dd2dt = (np.pi/12) * (q*b*d2-d*((24/(tx*.99729))**2+k*b)) + (1/mu)*fcd*dcdt        
        
        
        
        
        
        
        
        
        #H stuff
        tw = t-twake
        if (sleepstatus == 1):
            dhdt = -2 * (tw**1.25) * (rhw**2) * (h - uc)
            wakesleeparray.append(1.1)
        else:
            wakesleeparray.append(.95)
            dhdt = (1-.1*c) * rhsl * (uh - h)
        
        #CC stuff
        Ac = uc - a * np.e**(h/hac)
        CC = Ac* (.91 * c-.29*c2)
        
        #Cogt stuff -- Sum of the other things
        cogt = (.91 * c-.29*c2) + h 
        
        #append arrays
        harray.append(h)    
        carray.append(c)
        c2array.append(c2)
        tarray.append(t)
        cogtarray.append(cogt)
        CCarray.append(CC)
        warray.append(w)
        intensityarray.append(intensity(t))
        barray.append(b)
        darray.append(d)
        d2array.append(d2)
        
        #W stuff (is basically updates)
        if (sleepstatus == 0):
            if (h+CC >= np.abs(w0)):
                w = w0
            else:
                w = -(h+CC)
        else:
            dwdt = -rw * w
            w = w + dwdt*dt #wupdate
        
        #Updates
        c = c + dcdt*dt
        c2 = c2 + dc2dt * dt
        d = d + dddt * dt
        d2 = d2 + dd2dt * dt
        t = t+dt
        n=n+dndt*dt
        h = h+dhdt*dt
        
eulers()    
#plot stuff
plt.plot(tarray,darray,'blue')
plt.plot(tarray,carray,'red')
plt.plot(tarray,cogtarray)
plt.plot(tarray,wakesleeparray)
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.savefig("test.svg")



