def greet():
    print("Hello from first.py")

if __name__ == "__main__":
    # If this is a main file then the __name__ is __main__ because this is the file being called
    # to execute
    print("This is a program running the file")
else:
    # The __name__ is not = to __main__ because it is not the main file its being called 
    # from some other file
    print("This is a import")