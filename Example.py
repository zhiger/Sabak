import numpy as np

a = np.random.randint(0, 100, size=10)
b = [ value for value in a if value==1]
print(len(b))