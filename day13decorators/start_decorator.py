def start_function(func):
    def wrapper():
        print("start function")   
        func()                    # run the original function
        print("end function")     
    return wrapper

@start_function
def greet():
    print("hello user")

# Call the decorated function
greet()
