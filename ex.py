from math import *
# from cmath import *
# from sympy import *

# x=Symbol('x')
# a=Symbol('a')
# result = solve([-12*x**4*a - 18*x**3+5*x**2 + 10*x - 30],[x])
# # print(result[a])
# print(result)

# result2 = solve([-12*x**4 - 18*x**3+5*x**2 + 10*x - 30],[x])
# result2 = solve([(-18*x**3 + 5*x**2 + 10*x - 30)/(12*x**4) - sin(cos(x)).real],[x])
# result2 = solve([sin(cos(x))],[x])
# result2 = solve([-12*x**4*sin(cos(x)) - 18*x**3+5*x**2 + 10*x - 30],[x])
# print(type(result2))
# print(result2)

# x1 = str(result2[0][0])
# print(eval(x1))

# x2 = str(result2[1][0])
# print(eval(x2))


# print(result2)




# x1 = str(result[0][0])
# print(eval(x1))
# x2 = str(result[1][0])
# print(eval(x2))

# for i in range(len(result)):
#     for j in range(len(result[i])):
#         print('------')
#         print(result[i][j])

# a=x1.real
# b=x1.imag
        
# a = sin(cos(30))
# print(type(a))


import cmath
import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-7,5)
plt.plot(x,-12*x**4*sin(cos(x)) - 18*x**3+5*x**2 + 10*x - 30)
plt.show()