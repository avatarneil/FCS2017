import numpy as np
from scipy.optimize import minimize
from scipy.integrate import odeint
import matplotlib.pyplot as plt

init = [-5,-1]
initH = 15

tlist = np.linspace(0,100,101)
mu = .5
rhw=6.64*(10**-5)
rsw=1/2.14
uh=0.9896/24
sleepstatus = 1
hac=0.098
uc=.1503
a=6.2*10**-6
omega=(2*np.pi)/24
t0=18.24           
kappa=5

def objective(init,t,mu): #vanderpal
    x,y=init
    dxdt = mu*(x*omega**2-(1/3)*x**3-y)
    dydt = (1/mu)*x*omega**2
    dadt = [dxdt,dydt]
    return dadt

def homSleep(initH,t,uh,rsw):
     h=initH
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
    
def homWake(initH,t,t0,uh,rhw):
    h=initH
    #dhdt = -2*tw*((rhw)**2)*(uh-h)
    dhdt=((t**2)/(t+t0))*rhw*(h-uc)
    return dhdt
  
def testfunc(initB,t,kappa):
    alphata=initB
    didi = kappa*alphata
    return didi
    
def circadian(initC,t,uc,a,hac):
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
solTestFunc=odeint(testfunc,initH,tlist,args=(kappa,))
#solObjDriven = odeint(objectiveDriven,init,tlist,args=(mu,))
solhomSleep = odeint(homSleep,initH,tlist,args=(uh,rsw,))
solhomWake = odeint(homWake,initH,tlist,args=(uh,t0,rhw,))

circarray=[]
for i in range(len(tlist)):
    circarray.append(circadian(initH,tlist[i],uc,a,hac))
    
#solCircadian = odeint(circadian,init2,tlist,args=(uc,a,hac,))
#plt.plot(tlist, solObj[:, 0], '#008080', label='undriven')
#plt.plot(tlist, solhomSleep[:,0], 'r',label='solhomsleep')
#plt.plot(tlist, solObjDriven[:,0], 'r',label='driven')
#plt.plot(tlist, solhomWake[:,0], 'g',label='solhomWake')
#plt.plot(tlist, solTestFunc[:,0])
#plt.plot(tlist, circarray,'b', label='solcircadian')
plt.plot(tlist, solhomWake[:,0]+circarray, label='prod')
#plt.plot(tlist,circarray)
plt.xlim(0,54)
plt.ylim(-5,15)
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