#Python Program to Check if a Number is a Palindrome
num = int(input("enter the number: "))
reversed_num =  int(str(num)[::-1])
if reversed_num == num:
   print("palindrome")
else:
   print("neh")

  