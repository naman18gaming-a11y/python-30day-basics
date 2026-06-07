
# Create a generator that yields squares from 0 to n-1

def fun(n):
    for x in range(n):
        yield x ** 2

if __name__ == "__main__":
    for num in fun(5):
        print(num)

