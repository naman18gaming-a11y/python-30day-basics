#Unique Word Counter
from shlex import split
import string


def unique_word_counter(text):
    words = split(text)
    unique_words = set(words)
    return len(unique_words)

sentence = input("enter a sentence:")
print("the number of unique words in the sentence is:", unique_word_counter(sentence))