from matplotlib import pyplot as plt
import numpy as np


def Heaviside(x,step):
    list=[]
    for i in x:
        if i==0:
            list.append(step)
        elif i <0:
            list.append(0)
        else:
            list.append(1)
    return list

step=0.5

x=np.linspace(-10,10,100)

y=Heaviside(x,step)

plt.plot(x,y,label="Heaviside(x)")

plt.xlabel("Values of X")

plt.title("Activation Functions")

plt.ylabel("F(x)")

plt.legend()

plt.grid(True)

plt.show()