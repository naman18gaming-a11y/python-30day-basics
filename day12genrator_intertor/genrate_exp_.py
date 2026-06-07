# Create a generator expression that produces squares of numbers from 0 to 4
g = (i * i for i in range(5))
for num in g:
    print(num)