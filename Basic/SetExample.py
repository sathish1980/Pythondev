class setExample():
    def setconcepts(self):

        Fruits={"Banana","Apple","Watermelon"}
        print(Fruits)
        print(len(Fruits))
        for setvalue in Fruits:
            print(setvalue)
        Fruits.add("Orange")
        Fruits.add("Orange")
        print(Fruits)
        thisset = {"apple","banana","cherry"}
        mylist = ["kiwi","orange"]
        thisset.update(mylist) # list extends
        print(thisset)
        


obj=setExample()
obj.setconcepts()