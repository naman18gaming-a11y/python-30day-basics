# Python Program to Convert Binary to Gray Code
def bina_to_gray(n):
    n = int(n, 2)
    gray = n ^ (n >> 1)
    return bin(gray)[2:]


gray_code = bina_to_gray('1010')
print(gray_code,)