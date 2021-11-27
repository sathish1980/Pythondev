from Basic.secondclass import secondclass


class multilevel(secondclass):

    def gender(self,gen):
        if gen=="M":
            print("You are Male")
        elif gen == "F":
            print("You are Female")
        else:
            print("You are Transgender")
obj4 = multilevel(3,4)
obj4.gender("F")
obj4.mulmethod()
obj4.submethod()
obj4.div()