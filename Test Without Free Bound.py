import numpy as np
import matplotlib.pyplot as plt

M=9
x=np.linspace(0,1,M)
dx=1/(M-1)

N=17
T=2
t=np.linspace(0,T,N)
dt=T/(N-1)

lbda=dt/(dx**2)

b=1
S=[b]

def f(t:float)->float:
    return 1

def phi(x:float)->float:
    return 1-x

def Uinit(M:int)->list:
    U=[]
    x=np.linspace(0,1,M)
    for i in range(len(x)):
        U.append(phi(x[i]))
    return U

def Mat(M:int,lbda:float):
    d=np.ones(M)*(1+2*lbda)
    d1=np.ones(M-1)*(-lbda)
    return np.diag(d)+np.diag(d1,1)+np.diag(d1,-1)


U0=Uinit(M)
Uk=U0
########## BOUCLE ##########
for k in range(len(t)):
    if k==0:
        """
        Au temps t=0, on calcule uniquement l'emplacement du nouveau bord'
        """
        
        U0=Uinit(M)
        plt.plot(x,U0)
        plt.title("U0")
        plt.show()
    
    A=Mat(M,lbda)
    Uk=np.linalg.solve(A,Uk)
    
    plt.plot(x,Uk)
    plt.show()

    
        
        

        
