#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import math 
from sympy import diff, symbols 
import sympy as sympy 
a,b,x,y = symbols('a b x y ')
E=10**(-12)


# In[2]:


def f():
    return (y-3)/(x+3*x**2) 


# In[3]:


def p1():
    P=1/(3*x**2+1)
    a = diff(P,y) 
    return a
print('Частная производная P=',p1())


# In[4]:


def p2():
    Q=1/y-3
    b=diff(Q,x)
    return b
print('Частная производная Q=',p2())


# In[5]:


if p1() == p2(): 
    print("Является уравнением в полных дифференциалах ") 
else:
    print('Не является уравнением в полных дифференциалах')
        


# In[6]:


def F1(x):
    F1= 1/(x+3*x**2) 
    i = sympy.integrate(F1, x) 
    return i 


# In[7]:


def F2(y): 
    F2=1/(y-3) 
    i = sympy.integrate(F2, y) 
    return i 


# In[8]:


print(F2(y),'=',F1(x),'+ln|C|')



# In[10]:


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
print("Наш корень уравнения:",xi) 


# In[ ]:





# In[ ]:




