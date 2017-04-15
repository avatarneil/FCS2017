import numpy as np
from scipy.optimize import minimize
from scipy.integrate import odeint
import matplotlib.pyplot as plt

init = [-1,1]
init2 = 5
tlist = np.linspace(0,120,1200)
mu = .5
tw=1
rhw=(1/38)
rsw=1/2.14
uh=0.9896/24
sleepstatus = 1
hac=0.098
uc=.1503
a=6.2*10**-6
omega=(2*np.pi)/24

def objective(init,t,mu): #vanderpal
    x,y=init
    dxdt = mu*(x*omega**2-(1/3)*x**3-y)
    dydt = (1/mu)*x*omega**2
    dadt = [dxdt,dydt]
    return dadt

def homSleep(init2,t,uh,rsw):
     h=init2
     tindex=0
     dif = 100000000000
     ttest = 0
     for i in range(len(tlist)):
         ttest = abs(tlist[i]-t)
         if (ttest<dif):
             dif=ttest
             tindex=i
     dhdt = rsw*(1-.1*solObj[:,0][tindex])*(uh-h)
     return dhdt
    
def homWake(init2,t,tw,uh,rhw):
    h=init2
    #dhdt = -2*tw*((rhw)**2)*(uh-h)
    dhdt=-2*tw*(rhw**2)*(h-uh)
    return dhdt
def testfunc(init2,t,k):
    tfunc = init2
    dtfuncdt=k*tfunc
    return dtfuncdt    
def circadian(init2,t,uc,a,hac):
     #ifasleep, use sleep version of h, if awake use awake version
     tindex=0
     dif = 100000000000
     ttest = 0
     for i in range(len(tlist)):
         ttest = abs(tlist[i]-t)
         if (ttest<dif):
             dif=ttest
             tindex=i
     if(sleepstatus == 0):
         h = solhomSleep[:,0][tindex]
     else:
         h = solhomWake[:,0][tindex]
     Ac = uc-a*((np.e)**(h/hac))
     c = Ac*(.91*solObj[:,0][tindex]-.29*solObj[:,0][tindex]) 
     return c

def cogt(t):
    dif = 100000000000
    ttest = 0
    for i in range(len(tlist)):
        ttest = abs(tlist[i]-t)
        if (ttest<dif):
            dif=ttest
            tindex=i
    if(sleepstatus == 0):
        return solhomSleep[:,0][tindex] + solCircadian[:,0][tindex]
    else:
        return solhomWake[:,0][tindex] + solCircadian[:,0][tindex]



solObj = odeint(objective,init,tlist,args=(mu,))
solTestFunc=odeint(testfunc,init2,tlist,args=(1.5,))
solObjDriven = odeint(objectiveDriven,init,tlist,args=(mu,))
solhomSleep = odeint(homSleep,init2,tlist,args=(uh,rsw,))
solhomWake = odeint(homWake,init2,tlist,args=(uh,tw,rhw,))

circarray=[]
for i in range(len(tlist)):
    circarray.append(circadian(init2,tlist[i],uc,a,hac))
    
#solCircadian = odeint(circadian,init2,tlist,args=(uc,a,hac,))
#plt.plot(tlist, solObj[:, 0], '#008080', label='undriven')
#plt.plot(tlist, solhomSleep[:,0], 'r',label='solhomsleep')
#plt.plot(tlist, solObjDriven[:,0], 'r',label='driven')
#plt.plot(tlist, solhomWake[:,0], 'g',label='solhomWake')
#plt.plot(tlist, solTestFunc)
plt.plot(tlist, circarray,'b', label='solcircadian')
#plt.plot(tlist, solhomWake[:,0]+solCircadian[:,0], label='sum')
#plt.plot(tlist,circarray)
#plt.xlim(-1,20)
#plt.ylim(-5,15)
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.savefig("test.svg")

#def constraint1(x):
#    return x[0]*x[1]*x[2]*x[3]-25.0
#
#def constraint2(x):
#    sum_sq = 40
#    for i in range(4):
#        sum_sq = sum_sq - x[i]**2
#    return sum_sq


#bnds = (b,b,b,b)
#con1 = {'type':'ineq','fun': constraint1}
#con2 = {'type':'eq','fun':constraint2} 
#cons = [con1,con2]

#sol = minimize(objective,x0,method='SLSQP',\
               #bounds=bnds)

#print(sol.x)