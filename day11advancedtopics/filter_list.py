#Use filter() to keep numbers greater than 50.
numbers = [10,55,80,23,90]
sort = list(filter(lambda x: x> 50, numbers))
print(sort)