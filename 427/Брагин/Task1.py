import math
import numpy as np
import matplotlib.pyplot as plt


class Logarifm:
    def __init__(self):
        self.Arg =16
        self.answers_in_points = []
        self.schedule = []
        self.aboba = [1, 5, 10, 100]

    def func(self):
        for i in range(0, 101):
            try:
                y = math.log(2*i, math.fabs((math.exp(math.cos(i)**self.Arg)*math.tan(i**2))/((self.Arg/9)*i+math.sqrt(i**3))))
                self.schedule.append(y)
                if i == 1 or i == 5 or i == 10 or i == 100:
                    self.answers_in_points.append(y)
            except ZeroDivisionError:
                print('Нельзя делить на ноль, давай без этого...')

        for i in zip(self.answers_in_points, self.aboba):
            print(i[0], '- значение в точке', i[1])

    def plot(self):
        plt.subplots()
        x = np.arange(0, len(self.schedule), 1)
        plt.plot(x, self.schedule)
        plt.show()


a = Logarifm()
a.func()
a.plot()