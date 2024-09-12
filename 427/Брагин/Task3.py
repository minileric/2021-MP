import math


def f(x, y):
    v = (math.exp(y)) / ((1 + math.exp(x)) * y);
    return v;


def predict(x, y, h):
    y1p = y + h * f(x, y);
    return y1p;


def correct(x, y, x1, y1, h):
    e = 10 ** (-12);
    y1c = y1;

    while (abs(y1c - y1) > e + 1):
        y1 = y1c;
        y1c = y + 0.5 * h * (f(x, y) + f(x1, y1));

    return y1c;


def printFinalValues(x, xn, y, h):
    while (x < xn):
        x1 = x + h;
        y1p = predict(x, y, h);
        y1c = correct(x, y, x1, y1p, h);
        x = x1;
        y = y1c;

    print("The final value of y at x =",
          int(x), "is :", y);


if __name__ == '__main__':
    x = 0;
    y = 1;
    xn = 1;

    # step size
    h = 10 ** (-5);

    printFinalValues(x, xn, y, h);