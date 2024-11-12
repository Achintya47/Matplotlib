#Sigmoid, Tanh, ReLU and Heaviside Step Function
from matplotlib import pyplot as plt
import numpy as np

def Relu(x):
    list=[]
    for i in x:
        list.append(max(0,i))
    return list

def leakyReLU(x):
    list=[]
    for i in x:
        if i >0:
            list.append(i)
        else:
            list.append(0.01*i)
    return list


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

y1=1/(1+np.exp(-x)) #Sigmoid Range[0,1]

y2=(np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x)) #Tanh Range[-1,1]

y3=Relu(x)

y4=Heaviside(x,step)

y5=leakyReLU(x)

plt.plot(x,y1,label="Sigmoid(x)")

plt.plot(x,y2,label='Tanh(x)')

plt.plot(x,y3,label="ReLU(x)")

plt.plot(x,y4,label="Heaviside")

plt.plot(x,y5,label="LeakyReLU")

plt.xlabel("Values of X")

plt.title("Activation Functions")

plt.ylabel("F(x)")

plt.legend()

plt.grid(True)

plt.show()