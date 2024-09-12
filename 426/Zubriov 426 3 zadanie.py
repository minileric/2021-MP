import numpy as np
import math

#Zubrilov 22.11.2001
A=8
B=22
C=2001+11**3
func= lambda x: np.exp(A*x)+x**B+math.log(x**3,C)

a=0.001#начальное приближение
b=0.2
c=1
epsilon_1=10**(-12)#эпсилон для проверка
i=0
while(b-a>epsilon_1):
    c=(a+b)/2
    if(func(b)*func(c)<0): 
        print(a,"--",b)
        a=c
    else:
        b=c  
    i+=1
print(func(a))