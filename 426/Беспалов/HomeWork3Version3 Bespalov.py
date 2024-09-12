import numpy as np
import math


"""

Ну через рекурсию функциональненько ведь получается, так?)

"""


A = 8
B = 12
C = 2001+11**3

func = lambda x: np.exp(A*x)+x**B+math.log(x**3, C)         # отвратительная блин конструкция, фу


def function(a=0.001, b=0.5, eps=10**(-12), i=0):
    if b - a > eps:
        c = (a + b) / 2
        if func(b)*func(c) < 0:
            a = c
        else:
            b = c
        i += 1
        if b - a <= eps:                            # впихнул сюда дабы последний возврат рекурсии лишний убрать.
            print(
                '\n',
                a, '- корень' '\n',
                i, '- количество итераций', '\n',

            )
        function(a, b, eps, i)


function()
