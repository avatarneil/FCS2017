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


def intensity(z):
    if (z>=0 and z<=8):
        return .5
    else: 
        return 1500

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
    uh = .9896
    rhw = (1/32)
    uc = .1503
    
    #CC constants
    a = 6.2*10**-6
    hac = .098
    
    #W constants
    w0 = -.2868
    w=w0
    rw = (1/.86)
    
    #initial conditions
    c = -.17
    c2 = -1.22
    n = .5
    h = .5
    
    
    
    cbtmin = xmin + .8
    while t<=24:
        #C euler function
        
        #sleepwakecycle
        if (t>=0 and t<=8):
            sleepstatus = 0
        else:
            sleepstatus = 1
        
        #alpha&n -- Light stuff
        I = intensity(t)
        alpha = alpha0*(I/9500)**p
        dndt = 60*(alpha*(1-n)-beta*n)
        
        #b -- Driving function caused by light
        b = G * (1-n) * alpha * (1-.4*c) * (1-.4*c2)
        
        #C stuff
        dcdt = (np.pi/12) * (c2 + mu*(c/3+(4*c**3)/3-(256*c**7)/105)+ b)
        dc2dt = (np.pi/12) * (q*b*c2 - c*((24/tx*(.99729))**2 + k*b))
        
        #H stuff
        tw = t-twake
        if (sleepstatus == 1):
            dhdt = -2 * tw * rhw**2 * (h - uc)
        else:
            dhdt = (1-.1*c) * rhsl * (uh - h)
        
        #CC stuff
        Ac = uc - a * np.e**(h/hac)
        CC = Ac* (.91 * c-.29*c2)
        
        #Cogt stuff -- Sum of the other things
        cogt = CC + h + w
        
        #append arrays
        harray.append(h)    
        carray.append(c)
        c2array.append(c2)
        tarray.append(t)
        cogtarray.append(cogt)
        CCarray.append(CC)
        warray.append(w)
        
        #W stuff (is basically updates)
        if (sleepstatus == 0):
            print(t,'Asleep, updating w')
            if (h+CC >= np.abs(w0)):
                w = w0
            else:
                w = -(h+CC)
        else:
            print(t, 'Awake, updating w')
            dwdt = -rw * w
            w = w + dwdt*dt #wupdate
        
        #Updates
        c = c + dcdt*dt
        c2 = c2 + dc2dt * dt
        t = t+dt
        n=n+dndt*dt
        h = h+dhdt*dt
        
eulers()    
#plot stuff
plt.plot(tarray,warray,'blue',label='c')

plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.savefig("test.svg")



