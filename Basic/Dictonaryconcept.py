class dictonary():
    def dictonaryconcept(self):
        BikeBrands ={"Name":"Honda",
                     "Engine":"150cc",
                     "Price":"1lack",
                     "Color":("RED","Brown","Grey"),
                     "Name1": "Honda",
                     "Engine1": "150cc",
                     "Price1": "1lack",
                     "Color1": ("RED", "Brown", "Grey"),
                     "Name2": "Honda",
                     "Engine2": "150cc",
                     "Price2": "1lack",
                     "Color2": ("RED", "Brown", "Grey")
                     }
        print(BikeBrands)
        print(BikeBrands["Name"])
        print(BikeBrands["Engine"])
        print(BikeBrands.get("Engine"))
        listvalue=BikeBrands["Color"]
        for value in listvalue:
            print(value)
        print(BikeBrands["Color"])
        print(len(BikeBrands))
        print(BikeBrands.keys())
        listkeys=BikeBrands.keys()
        for eachvalue in listkeys:
            print(BikeBrands.get(eachvalue))
        print(BikeBrands.values())
        print(BikeBrands.items())

        if "Engine" in BikeBrands:
            BikeBrands["Engine"]="180cc"
            BikeBrands.update({"Engine": "210cc"})
            BikeBrands["Make"]= "2000"
            BikeBrands.update({"Make": "2002"})
            BikeBrands.update({"Height": "3ft"})
        print(BikeBrands)


obj=dictonary()
obj.dictonaryconcept()