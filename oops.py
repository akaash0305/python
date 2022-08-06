#encapsulation
#class reffered to multiple methods,variables and methods
class employee:
    mobile="samsung"
    model="876876"
    student="akash"
    rollno="1244"


    
    def apps(self):
        print(self.mobile,"\n",self.model)
        print("apps installed")
    
    def erase(self):
        print("apps are erased")
        mani=self.student+self.rollno
        print(mani)
    print("hello im sasi")

a1=employee()
a1.erase()
a1.apps()
'''#constructor
to paass the positional arguments we need in constructor
class students():
    studentsname=""
    rollno=""
    def display(self):
        print("students name",self.rollno)
        print("roll no",self.studentsname)
    def __init__(self,name,roll):
        self.studentsname=name
        self.rollno=roll
        print("iam constructor")
    def hello(self):
        print("hello")

a1=students("7890","akash")
a1.display()
a1.hello()
b1=students("ajay","7122")
b1.hello()
b1.display()

#Inheritance
class pet():
    def __init__(self):
        print("easy to mainten")
    def dog(self):
        print("human frindely")
class wildanimal(pet):
    def __init__(self):
        print("lion")
    def tiger(self):
        print("very danger")

b=wildanimal()
b.tiger()
a=pet()
a.dog()

#data hiding & private data base
class Hai:
    def __init__(self,a=0,b=0):
        self.__yet=a
        self.__bet=b
    def getYet(self):
        return self.__yet
    def __str__(self):
        return str(self.__yet)+ " "+ str(self.__bet)

h1=Hai(45,90)
print(h1.__yet)
print(h1.__bet)
print(h1.getYet())

class ak:
    def __init__(self,a=5,b=2):
        self.ben=a
        self.ten=b
    def __str__(self):
        return self.ben
    def bye(self):
        return (self.ben,self.ten)

a=ak()
print(a.ben)
print(a.ten)


class bat:
    def __init__(self,a=0,b=0):
        self.__car=a
        self.__key=b
    def ball(self):
        return self.__car
    def __str__(self):
        return str(self.__car)+" "+str(self.__key)

a=bat(10,20)
print(a)'''
    
#multiple inheritance

class jet:
    def intro(self):
        print("the types of jet.")
    def ramjet(self):
        print("they travel in supersonic speed.")

class airplane(jet):
    def boieng(self):
        print("its the famous manufacturing company.")
    def beldum(self):
        print("its second most famous manufacturing company.")
    
class chopers(airplane):
    def fiveblades(self):
        print("they are used in miltraybasis.")
    

class akash(chopers,airplane):
    def helium(self):
        print("they use white petrole.")
    def hotair(self):
        print("they use natural gas.")

obj_ak=jet()
obj_bk=airplane()
obj_ck=chopers()
obj_dk=akash()

obj_dk.beldum()
