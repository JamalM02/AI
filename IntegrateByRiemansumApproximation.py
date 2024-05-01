#Q1

import math


def integrate(f, a, b, n=1000):
    delta_x = (b - a) / n
    integral = 0
    for i in range(n):
        x_i = a + i * delta_x
        integral += f(x_i) * delta_x
    return integral


#f1(x)=x**3
def f1(x):
    return x ** 3


#f2(x)=x**3*sin(x)
def f2(x):
    return x ** 3 * math.sin(x)


#Range a&b
a = 0
b = 2

#Intgration for f1
print("Integral of f1(x) between", a, "and", b, ":", integrate(f1, a, b))

#intgration for f2
print("Integral of f2(x) between", a, "and", b, ":", integrate(f2, a, b))
