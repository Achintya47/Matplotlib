from matplotlib import pyplot as plt
import numpy as np

x=np.linspace(-10,10,100)

y=(np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x)) #Tanh Range[-1,1]

plt.plot(x,y,label="Tanh(x)")

plt.xlabel("Values of X")

plt.title("Activation Functions")

plt.ylabel("F(x)")

plt.legend()

plt.grid(True)

plt.show()
