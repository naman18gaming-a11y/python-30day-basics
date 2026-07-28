# Python Program to Count the Number of Words and Characters in a String
s = input("enter a string:")
char_count = len(s)
word_count = len(s.split()) if s.strip() else 0


print("Characters:", char_count)
print("Words:", word_count)