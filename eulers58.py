import numpy as np
import matplotlib.pyplot as plt
carray = []
c2array = []
tarray = []
harray = []
alertarray = []
wakesleeparray=[]

def eulers():
    dt = .01
    t = 0
    i = 0 
    
    #C constants -- There will be a million of them
    mu = .13
    q = (1/3)
    tx = 24.2
    k = .55
    beta = .013
    G = 19.875
    alpha0 = .16
    p=.6
    
    #initial conditions
    c = -.17
    c2 = -1.22
    n = .5
    
    
    sleepstatus=1
    
    cbtmin = xmin + .8
    while t<=24:
        
        #C euler function
        
        
        #alpha&n -- Light stuff
        alpha=alpha0*(I/9500)**p
        dndt = 60*(alpha*(1-n)-beta*n)
        n=n+dndt*t
        
        #b -- Driving function caused by light
        b = G * (1-n) * alpha * (1-.4*c) * (1-.4*c2)
        
        
        
        
        
        
        dcdt = (pi/12) * (c2 + mu*(c/3+(4*c**3)/3-(256*c**7)/105)+ b)
        dc2dt = (pi/12) * (q*b*c2 - c*((24/tx*(.99729))**2 + k*b))
        
        