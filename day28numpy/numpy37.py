import numpy as np
arr = np.array([10,20,30])
copy_arr = arr.copy()
view_arr = arr.view()
copy_arr[0]= 99
view_arr[0] = 67
print("Original array:", arr)
print("Copy array:", copy_arr)
print("View array:", view_arr)