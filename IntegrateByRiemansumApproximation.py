#Q1

import math


def integrate(f, a, b, n=1000):
    delta_x = (b - a) / n
    sum = 0
    for i in range(n):
        x_i = a + i * delta_x
        sum += f(x_i)
    return sum * delta_x


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
result_f1 = integrate(f1, a, b)
print("Integral of f1(x) between", a, "and", b, ":", result_f1)

#intgration for f2
result_f2 = integrate(f2, a, b)
print("Integral of f2(x) between", a, "and", b, ":", result_f2)
