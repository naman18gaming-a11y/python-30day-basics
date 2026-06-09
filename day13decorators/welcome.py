def start_function(func):
    def wrapper():
        print("welcome")   
        func()  
    return wrapper

@start_function
def greet():
    print("python")


greet()
