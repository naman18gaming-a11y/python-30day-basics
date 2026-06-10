# Create a generator that yields even numbers from 0 to n-1
def fun(n):

    for x in range(n):
        if x % 2 == 0:
            yield x

if __name__ == '__main__':
    for num in fun(10):
        print(num)