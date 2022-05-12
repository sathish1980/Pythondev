class List():

    def Listimplementation(self):
        Fruits=["Apple","Dragonfruit","Banana","Apple","Pineapple"]

        print(Fruits[1:4])
        Totallen=len(Fruits)
        for eachvalue in range(0,Totallen):
            print(Fruits[eachvalue])
        if "Banana" in Fruits:
            print("Exist")
        #Fruits[0:4]="Kiwi"
        #print(Fruits)
        Fruits.insert(2,"Watermelon")
        print(Fruits)
        Fruits.append("Mango")
        print(Fruits)
        Vegetables = ["brinjal", "onion", "Tomato"]
        Drinks = ["Coke", "Pepsi"]
        #Drinks.extend(Vegetables)
        Fruits.extend(Vegetables)
        print(Fruits)
        Fruits.remove("Apple")
        print(Fruits)
        Fruits.pop()
        print(Fruits)
        print(Vegetables)
        #del Vegetables[1]
        Vegetables.clear()
        print(Vegetables)
        for eachvalue in Fruits:
            print(eachvalue)
        for indexposition in range(0,len(Fruits)):
            print(Fruits[indexposition])
        i=0
        while i<len(Fruits):
            print(Fruits)
            i=i+1
        Fruits.sort(reverse=True)
        print(Fruits)


obj=List()
obj.Listimplementation()