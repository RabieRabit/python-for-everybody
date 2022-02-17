def dec(func):
    def some_func():
        print("This is before")
        func()
        print("This is after")
    return some_func

@dec
def greet():
    print("Hello Henry")

greet()


def decoration(func):
    def function():
        return func()**3
    return function

@decoration
def num():
    return 7

var = num()
print(var)