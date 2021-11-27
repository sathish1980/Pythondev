import random

print("Welcome")
"""print("to")
print("Besant")
print("Besant")
print("Besant")
print("Besant")
print("Besant")
print("Besant")
sat="Wlcome"""
print("last line")

a1 = "sathish's"
a = "value"
A =  '''sathish's
        kumar
        R '''
b = 2
c= "kumar"
d='s'
print(a)
print(a1)
print(type(a))
print(type(b))
print(type(c))
print(type(d))

e= 2.13
f=True
print(type(e))
print(type(f))

g=str(e)
print(type(g))

z=10
b=20
print(complex(z))

print(random.randrange(10, 100))
print(A)
print(len(A))

X=5
X+=2

print(X)

ca=1.2
cb = int(ca)
print(type(ca))
print(type(cb))


cc= " Sathish kumar.r is a Trainer "
cc1= "concat"
print(cc)
print(cc[3])
print(len(cc))
for asd in cc :
    print(asd)
print("trainers" in cc)
print("trainers" not in cc)
print(cc[2])
print(cc[2:])
print(cc[len(cc)-6:])
print(cc[:len(cc)-6])
print(cc[2:7])
print(cc)
print(cc.upper())
print(cc.lower())
print(cc.strip())
print(cc.replace("is","was"))
print(cc.replace("is","was",1))
print(cc.split("a"))
print(cc+cc1)
print(cc.count("a"))
cs="12sa"
print(cs.isalnum())
xa =12
xa +=12
xa = xa+12
print(xa)
xb = 13.2
xb += 1
xz=2
print(xa >10 and xb<20 and xz >10)
xc="sathish"
print(xa+xb)
print(xa-xb)
xy=36
if xy > 35:
    print("you are 35")
else:
    print("you are <35 ")
age =45

if age >=18:
    print("You are eligible to apply voter id")
    if age>60 and age> 80:
        print("you are eligible for senior consession")
        if age >80:
            print("you are eligible for super senior conseesion")
    elif age >=45:
        print("you will be eligible for senior in 15 years")
elif age >15:
    c = 18-age
    print("you are not eligble to apply for the next " + str(c) + " Years but you have consession")
elif age >10:
    c = 18-age
    print("you are not eligble to apply for the next " + str(c) + " Years but you will have 50%  consession")
elif age >8:
    c = 18-age
    print("you are not eligble to apply for the next " + str(c) + " Years but you will have 25%  consession")
else :
    c= 18-age
    print("you are not eligble to apply for the next " + str(c) +" Years" )

x=45
if x>10:
    pass

var =["sathish","kumar","R","B.tech"]
var1 =["sathish1","kumar1","R1","B.tech1"]
for c in var:
    print(c)
    for d in var1:
        e=len(d)
        f=d[0:e-1]
        if c==f:
            pass
        else:
            print(d)
    print("***********")

sat=1
for x in range(sat,10):
    print(x)

sat=10
max=50
for x in range(sat,max):
    if x==40:

        print(x)
        break
    else:
        print("number not macthed")
i=10
while i<50:

    #print(i)
    if i==30:
        print(i)
        break
    i=i+1

"""Book a ticket
input:
total no of ticket
per ticket cost
gender:
if gender is male
    discount =50% per ticket
    print(how much i have pay)
    print(how mucj is discount)
if gender is female
    discount = 55 % per
    ticket
    print(how
    i
    have
    pay)
    print(how
    much is discount)
other genders
    you are not eligible to book a ticket"""

