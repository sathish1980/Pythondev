from Basic.functionandclass import functional


class secondclass(functional):
    a=20
    b=75
    def div(self):
        try:
            i = 10
            j = 0
            l = i / j
            print(l)
            print("This is global variable " + str(self.b))
        except:
            Exception("This is an exception ")
            print("Exception occured")
        finally:
            print("This is Finally")


    def raise_func(self):
        i = 17
        if i < 18:
            raise Exception("You are not eligible")
            print("error")
        else:
            print("You are eligiblwe")

    def __init__(selfa,a,r):

        z=a+r
        print("This is constructor" +str(a)+str(r))
        print("This is constructor" + str(z))
"""obj2 = secondclass(5, 6)
obj2.div()
#obj2.raise_func()
obj2.firstmethod(3,6)
obj2.submethod()"""

