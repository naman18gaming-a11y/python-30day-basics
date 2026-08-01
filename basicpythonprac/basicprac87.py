#Python Program to Remove a Key from a Dictionary
dic = {'a': 1, 'b': 2, 'c': 3}
key = input("Enter the key to remove: ")
if key in dic:
    del dic[key]

    print(dic)