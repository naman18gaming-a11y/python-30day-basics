#Python Program to Check if a String is a Pangram or Not




import string


word = input("Enter a string: ")
alphabet = string.ascii_lowercase   

# Check each letter
for char in alphabet:
    if char not in word.lower():
        print("Not a pangram")
        break
else:
    print("Yes, it's a pangram")
     
    
