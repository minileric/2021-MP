#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math
from sympy import diff, symbols
import sympy as sympy
a,b,x, y = symbols('a b x y')


# In[2]:


E = 10^(-12) 
def main():
    
    def f():
        return (y-3)/(x+3*x**2)
    
    def dP():
        P = x+3*x**2
        a = diff(P,x)
        return a
    print("Значение производной  по Y для функции P =",dP())
    def dQ():
        Q= y-3
        b = diff(Q,y)
        return b
    print("Значение производной  по X для функции Q =",dQ())
   
    if dP() == dQ():
        print("Метод полных дифференциалов применим к нашей функции")
    else:
        print("Так как P  не равно Q,метод полных дифференциалов не применим к нашей функции. Найдем корни стандартным подходом.")
    def f1(y_0):# подсчет интеграла от dy/(y-3)
        f = 1/(y_0-3)
        i = sympy.integrate(f, y_0)
        return i
    def f2(x_0):# подсчет интеграла от dx/(x+3x^2)
        F = 1/(x_0+3*x_0**2)
        j = sympy.integrate(F, x_0)
        return j
        # выражение будет приведено к виду: ln|y-3| = ln|x/1+3x| + ln|c|
    def f3(x1,y1,c):# подсчет логарфмов
        q = np.log(y1-3)
        w = np.log(x1/(1+3*x1))
        e = np.log(c)
        return q,w,e
        
        # y-3 = x/(1+3x) + c1
        
    def func(o,c1):
        return 3*(c1*o +3*o +1)/(3*o-1)
    
    i=1
    o = np.linspace(0,100,1000)
    c1 = np.linspace(0,100,1000)
    y1=func(o[i],c1)
    xi=(o[i])
    while xi <= E:
        i+=1
        y1+=func(o[i],c1)
        xi=(o[i])
    #print(y1)
    print("Наш корень уравнения:",xi)
print(main())

