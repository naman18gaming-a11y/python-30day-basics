#Create a function that prints the multiplication table of a given number up to 10.
def multiplication_table(num):
    for i in range(1,11):
        print(f"{num} x {i} = { num * i }")
number = int(input("Enter a number to print its multiplication table: "))
multiplication_table(number)    