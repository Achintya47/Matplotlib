from matplotlib import pyplot as plt
import numpy as np

def Relu(x):
    list=[]
    for i in x:
        list.append(max(0,i))
    return list

x=np.linspace(-10,10,100)

y=Relu(x)

plt.plot(x,y,label="ReLU(x)")

plt.xlabel("Values of X")

plt.title("Activation Functions")

plt.ylabel("F(x)")

plt.legend()

plt.grid(True)

plt.show()