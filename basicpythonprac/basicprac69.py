#Python Program to Count the Occurrences of Each Word in a String
string = input("enter a string: ")
words = string.split()
for word in words:
    count = words.count(word)
    print(f"{word}: {count}")