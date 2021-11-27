
class functional:
    a=40
    def firstmethod(self,i,j):
        k=i+j
        print(k)
    def submethod(self):
        self.mulmethod()
        i=10
        #j=20
        j=self.retun_metod(3.5,7.1)
        k=i-j
        print(k)

    def retun_metod(self,j,e):
        l=j+e
        return l
    def mulmethod(self):
        i=10
        j=20
        k=i*j
        print(k)

"""obj = functional()
obj.firstmethod(4,5)
#mulmethod()
obj.submethod()"""
