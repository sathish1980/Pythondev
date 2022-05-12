
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
    def reverseaString(self):
        name="sathish"
        charvalue=[char for char in name]
        length=len(charvalue)
        print(charvalue)
        print(length)
        for i in range(length):
            i=length-1
            if(length>=0):
                print(charvalue[i])
                length=length-1


obj = functional()
obj.reverseaString()
