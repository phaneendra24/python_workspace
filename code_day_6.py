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
