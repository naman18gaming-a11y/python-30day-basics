#Python Program to Remove a Key from a Dictionary
key = input("Enter the key to remove: ")
dic = {'a': 1, 'b': 2, 'c': 3}
if key in dic:
    del dic[key]
print(dic)