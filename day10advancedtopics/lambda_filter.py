#filter and filter()
numbers = [12, 7, 20, 5, 18, 3]
num = [list(filter(lambda x: x>10,numbers))]
print(num)