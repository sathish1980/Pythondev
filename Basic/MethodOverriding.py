from Basic.MethodOverloading import MethodOverloading


class MethodOverriding(MethodOverloading):
    def overridingconcept(self):
        print("overriding conecpt")
    def add(self,a,b):
        print("Child class implementation: "+str(a+b))
obj=MethodOverriding()
obj1=MethodOverloading()
obj.overridingconcept()
obj.add(4,5)
obj1.add(4,1)
#obj.add(2,3)
#obj1.add(2,3)