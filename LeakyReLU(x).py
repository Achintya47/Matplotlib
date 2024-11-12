from matplotlib import pyplot as plt
import numpy as np

def leakyReLU(x):
    list=[]
    for i in x:
        if i >0:
            list.append(i)
        else:
            list.append(0.01*i)
    return list


x=np.linspace(-10,10,100)

y=leakyReLU(x)

plt.plot(x,y,label="Leaky ReLU(x)")

plt.xlabel("Values of X")

plt.title("Activation Functions")

plt.ylabel("F(x)")

plt.legend()

plt.grid(True)

plt.show()