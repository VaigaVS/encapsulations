class myClass:
    __pivateVar=27;
    def __privMeth(self):
        print("I am inside class MyClass")

    def hello(self):
        print("Private Variable value",myClass.__pivateVar)

foo=myClass()
foo.hello()
foo.__pivateMeth()

