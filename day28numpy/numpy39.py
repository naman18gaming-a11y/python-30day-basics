import numpy as np


matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Print 50
print("Element 50:", matrix[1, 1])  

# Print entire second row
print("Second row:", matrix[1, :])   

# Print entire first column
print("First column:", matrix[:, 0]) 