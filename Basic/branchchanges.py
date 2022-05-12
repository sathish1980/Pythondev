import re


class branchchag:
    def reg(self):
        txt = "The rain in Spain"
        x = re.search("^The.*Spain$", txt)
        print(x)
        xc = re.split("\s",txt)
        print(xc)
        xcd = re.sub("rain", "RAIN", txt)
        print(xcd)
        name = "satish"
        xcc = re.search("[A-Z]$", txt)
        print(xcc)
    def txt_file_read(self):
        txt_file=open("C:\\Users\\sathishkumar\\PycharmProjects\\pythonBasics\\InputFile\\Env.txt","r")
        #print(txt_file.read())
        print(txt_file.readline())
        print(txt_file.readline())
        print(txt_file.readline())

        for x in txt_file:
            #print(x)
            list_value=re.split("-",x)
            if "Arun " in list_value:
                print("Yes")
        txt_file.close()
        txt_file1 = open("C:\\Users\\sathishkumar\\PycharmProjects\\pythonBasics\\InputFile\\Env.txt", "a")
        txt_file1.write("NEw column added")

        txt_file1.close()



obj = branchchag()
obj.txt_file_read()
