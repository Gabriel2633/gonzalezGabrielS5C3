import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from numpy import genfromtxt
from random import randint 

circuito = genfromtxt("CircuitoRC.txt",delimiter=" ")
circuito = pd.DataFrame(data=circuito)
print circuito.head()

plt.figure()
plt.scatter(circuito[0],circuito[1])
plt.show()

yv=circuito[1]
yvv=circuito[0]
def L(yv,y):
    l=np.exp(-(1.0/2.0)*sum((yv-y)**2)    
    return l

Mcam=empty((0))
Bcam= empty((0))

Mgues=randint(1.0,20.0)
Bgues=randint(1.0,20.0)

Mcam= append(Mcam,Mgues)
Bcam= append(Bcam,Bgues)

def g(t,R,C):
	V0=10.0
	Qmax=V0*C
	F= Qmax*((1)-(np.exp(-t/RC)))
	return F

cun= g(yvv,Mcam[0],Bcam[0])


lcam=empty((0))
lcam=append(lcam,L(yv,cun))

N=1000
for i in range(N):
    mp=np.random.normal(Mcam[i],0.1)
    bp=np.random.normal(Bcam[i],0.1)
    
    yI=g(yvv,Mcam[i],Bcam[i])
    yP=g(yvv,mp,bp)
    
    lP= L(yv,yP)
    lI= L(yv,yI)
            
    alpha=lP/lI    

    if(alpha>=1.0):

        Mcam= append(Mcam,mp)
        Bcam= append(Bcam,bp)
        lcam=append(lcam,lP)

    else:        

      beta=randint(0.0,1.0)

          if (beta<=alpha):
          
              Mcam= append(Mcam,mp)
              Bcam= append(Bcam,bp)
              lcam=append(lcam,lP)
          else: 
              Mcam= append(Mcam,Mcam[i])
              Bcam= append(Bcam,Bcam[i])
              lcam=append(lcam,lI)
      
plt.figure()
plt.scatter(Mcam,Bcam)
plt.show()