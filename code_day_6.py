'''
    exception handling-
        when there is exception, the developer does not want interuption or disturbance in the program
        flow. To acheive this we are using exception handling. 
'''

# a=100
# b=0

# #tyr :# your are telling this may have error u try
# try:
#     print(a/b)
# #expecept exception : you are saying if error thr i handle 
# #print("cant divide any number by zero")
# except ValueError as e:
#     print("invalid value :",e)

# except Exception as e:
#     print("please note ,number cant be divide by zero :",e)

# print("bye")

# raising your own exceptions 
# a=4 

# if a-4 ==0:
#     raise Exception("your condition sucks")
# else:
#     print("what are you even trying to do")


'''
oops- object oreinted programming structure
    - It's an efficeint concept used in all object oreinted languages like java and python.
    for multiple reasons we use oops concepts for example - code reusability,data security,data hiding.

    class -It's a blueprint -eg:birds,laptops.
    object - It's a thing created using class.
    note- one class can have multiple objects.

    eg:birds,laptops are class  and  parrot,hp. 
'''

# class employee:
#     def __init__(self,name,num) -> None:
#         self.name= name
#         self.num= num
#     def display(self):
#         print(self.name,"is an employee with no",self.num)

# dongle = employee("dongle",9)
# dongle.display()

'''
FLAMES
'''

# name1_list = [name for name in input("enter name : ")]
# name2_list = [name for name in input("enter name : ")]

# for i in name1_list:
#     if i in name2_list:
#         name1_list.remove(i)
#         name2_list.remove(i)
# count = len(name1_list)+len(name2_list)
# f_list = ["F","L","A","M","E","S"]

# f_dict = {
#     "F" : "friends",
#     "L" : "Love",
#     "A" : "affection",
#     "M" : "marraige",
#     "E" : "enemy",
#     "S" : "sister"
# }

# while(len(f_list)!=1):
#     if count > len(f_list):
#         count = len(f_list) % count

#     for i in range(count+1):
#         print("a")
#         print(count)
#         print(i)
#         if(count==i):
#             print(f_list.pop(i))
#             f_list.pop(i)
#     print("b")
#     break
            

# print(f_list)

'''
Lambda function - It is called as anonymous functions when we want to use functions concept alone
 without using function name there we apply concept  of lamba function 
'''

# list1 = [1,2,3]

# nList = map(lambda n:n+1,list1)

# nL = [i+i for i in list1]

# print("nl",nL)
# print(list(nList))


# l_names = ["someone strange" ,"people"]

# (lambda name:print(name))(l_names)

# powers = map(lambda n:pow(n,2),list1)

# print(list(powers))
'''
After creating a list with even numbers within the range 1 to 15. Now apply lambda function and create
a new list which should have square roots of the elements
'''
# import math
# listnum = [math.sqrt(x) for x in range(1,16) if x%2==0]
# newlist = map(lambda x:math.sqrt(x),listnum)
# print(list(newlist))

'''
Four pillars of OOPS-
    1) abstraction - Hiding the implementation part and showing what is required for the users
        eg: exe files
        we can make class or method as abstract , opposite to abstractors concrete 
    2) encapsulation - Binding dataand fuction into a single entity 
        public - one class info can be accessed by any other class 
        private - can used where it is declared /no in inheritected class
        protected - can be acceseed only where it got declared .. whichever class inherited from this classss there also we can use
    3) inheritance- Base class and derived class
        Derived class will inherit properties of base class 
        Base class - parent class 
        Derived class =child class
    4) polymorphism
'''


# abstraction
# from abc import ABC,abstractmethod

# class abstractedFish(ABC):
#     @abstractmethod
#     def curry(self):
#         print("Asdfasd")
#     @abstractmethod
#     def fried(self):
#         None

# class NrmlFish(abstractedFish):
#     def curry(self):
#         print("Yeah its curry")    
#     def fried(self):
#         print("Yeah its fried")

# customer = NrmlFish()
# customer.curry()
# customer.fried()

# inheritance

'''Types of inheritance -
    1- single inheritance
    2- multiple inheritance
    3- multi-level inheritance
    4- heirarical inheritance
    5- hybrid inheritance
'''
# single inheritance
# class parent():
#     def assets(self):
#         print("Get out")

# class child(parent):
#     def haveassets(self):
#         print("No")

# money = child()

# money.haveassets()
# money.assets()

# class A():
#     extras =30
# class B(A):
#     def getMarks(self):
#         submarks =70
#         print(self.extras + submarks)

# obj = B()

# obj.getMarks()

#multiple inheritance 

# class A():
#     labs =30
# class B():
#     extras1 =40
# class C(B,A):
#     def getMarks(self):
#         submarks =70
#         print(self.labs+ self.extras1 + submarks)

# obj = C()

# obj.getMarks()

# multi-level inheritance

# class grandParent():
#     def displayGp(self):
#         print("grandparent")
# class parent(grandParent):
#     def displayP(self):
#         print("parent")
# class child(parent):
#     def displayCh(self):
#         print("child")

# person = child()
# person.displayCh()
# person.displayP()
# person.displayGp()

# heirarical inheritance
# class parent():
#     def displayGp(self):
#         print("parent")
# class child1(parent):
#     def displayP(self):
#         print("child1")
# class child2(parent):
#     def displayCh(self):
#         print("child2")

# obj = child1()
# obj.displayGp()
# obj.displayP()

#hybrid inheritance

# class parent():
#     def pdisplay(self):
#         print("parent")

# class child1(parent):
#     def child1(self):
#         print("child1")

# class child2(parent):
#     def child2(self):
#         print("child2")

# class grandchild1(child1):
#     def grandchild1(self):
#         print("grandchild1")

# class grandchild2(child1):
#     def grandchild2(self):
#         print("grandchild2")

# class sgrandchild1(child2):
#     def sgrandchild1(self):
#         print("sgrandchild1")

# class sgrandchild2(child2):
#     def sgrandchild2(self):
#         print("sgrandchild2")

# obj1 = sgrandchild1()

# obj1.pdisplay()
# obj1.child2()
# obj1.sgrandchild1()

# obj2 = sgrandchild2()

# obj1.pdisplay()
# obj1.child2()
# obj1.sgrandchild1()

# a => public 
# _b => protected -can be accesed only where it is declared
# __c => private

# num  = input("enter your number :")
# while(int(num)!=1):
#     num = str(sum([int(i)*int(i) for i in num]))
#     if(len(num)==1 and num != 1):
#         print("Not happy number")
#         break
#     if(len(num)==1 and num ==1):
#         print("happy number")
#         break
# num  = input("enter your number :")
# while(int(num)!=1):
#     num = str(sum([int(i)*int(i) for i in num]))
#     if int(num)==1:
#         break
#     if(len(num)==1):
#         print("not a happy number")
#         break
# if(int(num)==1):
#     print("happy number")