import numpy as np
import matplotlib.pyplot as plt
carray = []
c2array = []
tarray = []
harray = []
alertarray = []
wakesleeparray=[]

def intensity(z):
    return 50000

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
    rw = (1/.86)
    
    #initial conditions
    c = -.17
    c2 = -1.22
    n = .5
    
    
    
    cbtmin = xmin + .8
    while t<=24:
        #C euler function
        #alpha&n -- Light stuff
        I = intensity(t)
        alpha = alpha0*(I/9500)**p
        dndt = 60*(alpha*(1-n)-beta*n)
        
        #b -- Driving function caused by light
        b = G * (1-n) * alpha * (1-.4*c) * (1-.4*c2)
        
        #C stuff
        dcdt = (pi/12) * (c2 + mu*(c/3+(4*c**3)/3-(256*c**7)/105)+ b)
        dc2dt = (pi/12) * (q*b*c2 - c*((24/tx*(.99729))**2 + k*b))
        
        #H stuff
        tw = t-twake
        if (sleepstatus == 1):
            dhdt = -2 * tw * rhw**2 * (h - uc)
        else:
            dhdt = (1-.1*c) * rhsl * (uh - h)
        
        #CC stuff
        Ac = uc - a * np.e**(h/hac)
        CC = Ac* (.91 * c-.29*c2)
        
        #W stuff
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
        t = t+dt
        n=n+dndt*dt
        h = h+dhdt*dt
        
        
        
        