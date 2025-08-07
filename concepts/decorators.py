def my_deco(func):
    def wrapper():
        print("Before function run")
        func()
        print("After function run")
    return wrapper

def hello ():
    print ("hello world")

@my_deco
def hello_deco():
    print ("hello world with decorator")
hello_deco()    