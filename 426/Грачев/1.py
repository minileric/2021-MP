# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 20:27:49 2021

@author: Vadim
"""

import math
import numpy as np
from matplotlib import pylab as plt

def func (x):
    result_1 = (np.e**(np.cos(x)**A)*np.tan(x**2))
    result_2=(A/9*x + np.sqrt(x**3))
    result = math.log(math.fabs(result_1/result_2),2) #result_1/result_2
    return result


def laba (x):
    result = (np.e**2/np.log(x)*x**3/22*np.sqrt(14*x))/x**2
    return result
x=[1,5,10,100]
A=20#Дата рождения!
y=[func(i) for i in x]
print ("Массив значений для ф-ции=",y)

x=[i for i in np.arange(2,100,10)]
y=[laba(i) for i in x]
fig = plt.figure( dpi=100)
plt.errorbar(x, y, xerr=3, yerr=4)
plt.grid()
plt.text(60, .030, '$  e^{2}/log(x)*x^{3}/22*\sqrt{14*x}/ x^{2} $')

plt.show()
