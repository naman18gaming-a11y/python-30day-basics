#Username Formatter
from shlex import join


username = input("enter the username:")
if len(username) < 5:
    print("username must be at least 5 characters long")
elif len(username) > 15:
    print("username must be less than 15 characters long")
else:
    print("username is valid")
    formatted_username = username.lower().replace(" ", "_")
    print("the formatted username is:", 
           formatted_username)
