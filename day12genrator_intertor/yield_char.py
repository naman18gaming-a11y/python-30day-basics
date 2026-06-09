# yield_square.py (example for characters)

def generate_chars(word):
    """Generator that yields characters of a string"""
    for ch in word:
        yield ch

# Using the generator
for c in generate_chars("PYTHON"):
    print(c)
