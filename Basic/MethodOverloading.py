class MethodOverloading():
    def overloadingconcpt(self,name=None,age=None):
        if(name!=None and age !=None):
            print(name + " : "+str(age) )
        elif (age==None):
            print(name)
    def add(self,a,b):
        print(a+b)
    def addition(self,a=None,b=None,c=None,d=None):
        if (a!=None and b!=None and c==None and d==None):
            print(a+b)
        elif(a!=None and b!=None and c!=None and d==None):
            print(a + b + c)
        elif (a != None and b != None and c != None and d!=None):
            print(a + b + c+d)
    def stringoverloading(self,a):
        var=type(a)
        if type(a)==var:
            print("This is string")
        elif type(a)==var:
            print("This is Integer")

        #print(a+b)
obj=MethodOverloading()
obj.addition(2,3,6)
obj.stringoverloading("sathish")
#obj.overloadingconcpt("sathish")
#obj.overloadingconcpt("sathish",23)
