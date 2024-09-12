#!/usr/bin/env python
# coding: utf-8

# ### Написать в функциональном стиле задачу приближенного вычисления корней функции
# 
# $$y-xy'=3(1+x^2y')$$
# $\newline$ С точностью $\epsilon = 10^{-12}$
# 
# #### Выполнил студент группы 425 Бибин Александр

# In[1]:


import numpy as np
import math
from sympy import diff, symbols
import sympy as sympy
a,b,x, y = symbols('a b x y')

def func():
    
    def g():
        return (y-3)/(x+3*x**2)
    
    def polnoe1():
        R = y-3
        a = diff(R,y)
        return a
    print("Значение производной  по y для функции R =",polnoe1())
    def polnoe2():
        S = x+3*x**2
        b = diff(S,x)
        return b
    print("Значение производной  по x для функции S =",polnoe2())
    E = 10^(-12) 
    if a == b:
        print("Метод полных дифференциалов является применимым к нашей функции")
    else:
        print("Так как R  не равно S,метод полных дифференциалов не применим к нашей функции. Найдем корни стандартным подходом.")
    
    # подсчет интеграла от dy/(y-3)
    def f1(y_0):      
        f = 1/(y_0-3)
        i = sympy.integrate(f, y_0)
        return i
    
    # подсчет интеграла от dx/(x+3x^2)
    def f2(x_0):
        F = 1/(x_0+3*x_0**2)
        j = sympy.integrate(F, x_0)
        return j
    # выражение будет приведено к виду: ln|y-3| = ln|x/1+3x| + ln|c|
        
    # подсчет логарфмов
    def f3(x1,y1,c):
        q = np.log(y1-3)
        w = np.log(x1/(1+3*x1))
        e = np.log(c)
        return q,w,e
        # учитывая, что все функции находятся под логарифмами с одним и тем же основанием, то логарифмы можно убрать.
        # y-3 = x/(1+3x) + c1
        
    def func(o,c1):
        return 3*(c1*o +3*o +1)/(3*o-1)
    
    i = 1
    o = np.linspace(0,100,1000)
    c1 = np.linspace(0,100,1000)
    y1 = func(o[i],c1)
    xi = (o[i])
    while xi <= E:
        i+=1
        y1+=func(o[i],c1)
        xi=(o[i])
    
    print("Корень уравнения:",xi)
print(func())


# In[ ]:




