#Python Program to Reverse a String using Recursion
string = "notion"

def rev(s=None):
    if s is None:
        s = list(string)   
    if len(s) == 0:        
        return
    print(s.pop(), end='') 
    rev(s)                 
rev()
