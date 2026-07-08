import numpy as np
a = np.arange(1,11)
even_numbers= np.where(a%2==0)
print(a)
print("Even numbers are at indices:", even_numbers)