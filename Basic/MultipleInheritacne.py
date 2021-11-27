from Basic.Multiplesecond import mulitplesecond
from Basic.functionandclass import functional


class multiple(functional,mulitplesecond):
    def multipleinhritance(self):
        print("multiple inheritance")

obj3=multiple()
obj3.multipleinhritance()
obj4= mulitplesecond()
obj4.mulmethod()
obj3.mulmethod()
obj3.submethod()
obj3.address()
