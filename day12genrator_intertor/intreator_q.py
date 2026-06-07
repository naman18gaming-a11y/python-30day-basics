# Create an iterator from a list
num = [100, 200, 300]
it = iter(num)

while True:
    try:
        print(next(it))
    except StopIteration:
        print("end")
        break