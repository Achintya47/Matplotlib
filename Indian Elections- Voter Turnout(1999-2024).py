from scipy import stats
from matplotlib import pyplot as plt
import numpy as np


Years=[1951,1957,1962,1967,1971,1977,1980,1984,1989,1991,1996,1998,1999,2004,2009,2014,2019,2024]
Turnout=[44.87,45.44,55.42,61.04,55.27,60.49,56.92,63.56,61.95,56.73,56.94,61.97,59.99,58.07,58.19,66.4,67.4,65.79]

slope, intercept, r, p, std_err = stats.linregress(Years, Turnout) 

predval=[]

myline=np.linspace(1951,2025,20)

regr=np.poly1d(np.polyfit(Years,Turnout,3))


def regression(x):
    return slope*x + intercept

predval=list(map(regression,Years))

plt.plot(Years,Turnout,label="Voter Turnout")
plt.plot(Years,predval,label="Linear Trend")
plt.plot(myline,regr(myline),label="Polynomial Trend")

plt.title("Voter Turnout Through the Years")

plt.xlabel("Years")
plt.ylabel("Turnout%")

plt.legend()
plt.grid()
plt.show()
