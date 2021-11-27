class listconcept:

    def listcon(self):
        subject=["Maths","Science","computer"]
        print(subject)
        print(subject[0])
        if "english" in subject:
            print("yes it avaialble")
        else:
            print ("No its not avaialble")
        print("******************")
        for xc in subject:
            print(xc)
            if xc == "Science":
                print("yes it avaialble")
            else:
                print("No its not avaialble")
        #subject[1] = "Bio-Science"
        #print(subject)
        subject[1:3] = ["Bio-Science","Computer science","Physics"]
        print(subject)
        subject.append("chemistry")
        print(subject)
        subject.remove("Physics")
        print(subject)
        subject.pop(1)
        print(subject)
        #del subject
        print(subject)
        student= tuple(("sathish",1,True,"kumar","R"))
        print(student)
        print(len(student))
        #print(student[1:3])
        if "kumar" in student:
            print("yes")
            s=list(student)
            print(s)
            s.append("B.tech")
            print(s)
            print(student)
            #del student
            print(student)
        else:
            print("no")
        for X in student:
            print(X)
            if(X == "kumar"):
                print("yes")
        xc= len(student)
        print(xc)
        print("@@@@@@@@@@@@@@@@@@@")
        for intr in range(0,xc):
            print(student[intr])
        setvalue = {"satish","kumar","B.tech","R"}
        print(setvalue)
        print(len(setvalue))
        for Xsd in setvalue:
            print(Xsd)
        thisset = {"apple","banana","cherry"}
        mylist = ["kiwi","orange"]
        thisset.update(mylist)
        print(thisset)

        thisset = {"apple", "banana", "cherry"}
        mylist = ["kiwi", "orange"]
        mylist.append(thisset)
        print(mylist)

        dict={"fname1":"sathish","lname1":"kumar","DOB":"1105","fname2":"sathish1","lname2":"kumar1","DOB2":"9999"}
        print(dict)
        print(dict["fname2"])
        print(len(dict))
        print(dict.get("lname2"))
        print(dict.keys())
        print(dict.values())
        print(dict.items())

        for XCV in dict:
            print(XCV +":"+dict[XCV])






obj1= listconcept()
obj1.listcon()
