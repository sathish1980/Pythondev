class Tuple():

    def tupleconceptes(self):

        Drinks=("Coke","Pepsi","Bovonto")
        print(Drinks)
        print(len(Drinks))
        print(type(Drinks[0]))
        NewTuple=("Coke",2,True)
        print(NewTuple[-1])
        if True in NewTuple:
            print("Yes")
        print(type(Drinks))
        listconvertion=list(Drinks)
        print(type(listconvertion))
        listconvertion.append("Frooti")
        Tupleconvertion=tuple(listconvertion)
        print(Tupleconvertion)

obj= Tuple()
obj.tupleconceptes()