#Using filter():
lists = [1,2,3,4,5,6,7]
num = list(filter(lambda x : x % 2 == 0 , lists))
print(num)