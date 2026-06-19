#Python Program to Find Numbers which are Divisible by 7 and Multiple of 5 in a Given Range
for num in range(1,100):
    if num % 7 == 0 and num % 5 == 0 :
        print("nums are:",num)