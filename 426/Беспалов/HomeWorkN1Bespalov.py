import math
import numpy as np
import matplotlib.pyplot as plt


class HomeWork1:
    def __init__(self):
        self.A = 12                                         # мой день рождения, он в ноябре. Не против подарочка в мае
        self.answers_in_points = []
        self.schedule = []

    def func(self):
        for i in range(1, 101):
            try:
                y = math.log(2*i, math.fabs((math.exp(math.cos(i)**self.A)*math.tan(i**2))/((self.A/9)*i+math.sqrt(i**3))))
                self.schedule.append(y)
                if i == 1 or i == 5 or i == 10 or i == 100:
                    self.answers_in_points.append(y)
            except ZeroDivisionError:
                print('Родной, на ноль делить нельзя, я эту точку считать не собираюсь')  # нет ну можно конечно, но нет

        print(
            'Значения в точках x = 1, 5, 10, 100', '\n',
            *self.answers_in_points
              )

    def schedule_plot(self):
        plt.subplots()
        x = np.arange(0, len(self.schedule), 1)             # да хитрюга и что
        plt.plot(x, self.schedule)
        plt.show()


a = HomeWork1()
a.func()
a.schedule_plot()
