import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-5,5,100)

y=1/(1+np.exp(-x))

plt.plot(x,y)

plt.xlabel("x")

plt.ylabel("Sigmoid (x)")

plt.grid()

plt.show()