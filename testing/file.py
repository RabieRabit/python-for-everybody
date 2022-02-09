class MyClass:
    #Default values
    par1 = "Default"

    #initilizing class
    def __init__(self, par1):
        self.par1 = par1

    #another function
    def another_class(self, par1 = "Thing"):
        self.par1 = par1

#Defining object
new_class = MyClass("First par")

new_class.another_class()

print(new_class.par1)
#type
print(type(new_class))