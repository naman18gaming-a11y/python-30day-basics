#random password genrator
import string 

password = input("enter the password: ")

pass_num = any(char in string.digits for char in password)
pass_letter = any(char in string.ascii_letters for char in password)
pass_special = any(char in string.punctuation for char in password)
if pass_letter and pass_num and pass_special :
    print("print strong password:")
else:
    print("Weak password! Please add missing character types.")
    print("Your password needs to include:")
    if not pass_letter: print("- At least one letter")
    if not pass_num:  print("- At least one number")
    if not pass_special: print("- At least one special")