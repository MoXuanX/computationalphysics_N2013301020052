def X(x,t):
    dxdt=40
    return dxdt
x0=0
import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,10,100)

from scipy.integrate import odeint
sol=odeint(X,x0,t)
print sol

plt.title('X(t)-t',size=20)
plt.xlabel('t/s',size=15)
plt.ylabel('x/m',size=15)
plt.plot(t,sol, color="red", linewidth=1.5, linestyle="-", label="X(t)=vt,v=40m/s")
plt.legend(loc='upper left')

plt.savefig('Homework4.png', format='png')

plt.show()
