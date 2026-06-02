# Character Frequency Counter
def char_freq_counter(string):
    freq = {}
    cleaned_string = string.replace(" ", "")
    for char in cleaned_string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
print(char_freq_counter("hello world"))
