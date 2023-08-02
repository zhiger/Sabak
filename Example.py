import numpy as np

a = np.random.randint(0, 100, size=10)
b = [ value for value in a if value==1]
c = len(b)
# print(c*2)

def func(param):
    return param*2

print(func(c))