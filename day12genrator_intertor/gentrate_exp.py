#Create a generator expression that produces:
def fun():
    yield 1
    yield 2
    yield 3

# Iterate over generator
for val in fun():
    print(val)
