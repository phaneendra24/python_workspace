#random package
import random as r

a = r.random()

print(a)
print(r.randint(10,20))

a=[ r.randint(1,20) for x in range(6) ]

print(r.choices(a,k=3))

print(dir(a))


# display whole year calender

import calendar

print(calendar.calendar(2022))
calendar.setfirstweekday(calendar.TUESDAY)
print(calendar.month(2023,9))
print(calendar.isleap(2024))
print(dir(calendar))

# displaying the date and time
import datetime

a= datetime.datetime.now()

sv = a.strftime("%y")
sv2 = a.strftime("%Y")
print(sv,sv2)

# functions 
#types classsifications-
#predefined functions
# userdefined funcitons 
'''
For code reusability we use function . If we want to use particular code multiple times in our 
program instead of writing the same code multiple times we can write it once include that inside a function and 
can call the function whereever we need it.
Types:
1- functions without arguments and without return values.
2- functions without arguments and with return values.
3- functions with arguments and with return values.
4- functions with arguments and without return values.
'''

a=0
def sameple(a:int):
     a=a+1 
     print(a)
     sameple(a) if a<10 else None
sameple(a)


# lemons program using functions type 1

lemons_to_be_given= 21

def check_lemons(lemons_to_be_given):
    lemons =int(input("enter your no of lemons:"))
    print(f"you have given {lemons - lemons_to_be_given} more") if lemons >lemons_to_be_given else print(f"{lemons_to_be_given-lemons} more needed")

check_lemons(lemons_to_be_given)



# find factors of the given number using functions type 2 

num = int(input("enter your number: "))

def factorsofnum(num):
    factors = [x for x in range(1,num+1) if num %x==0]
    print(factors)

factorsofnum(num)



# print mutliplication table of the given number using functions type3

num = int(input("enter your table number :"))
flag=1
def multiply(num,flag):
    if flag<13:
        print(f"{num} x {flag} = {num*flag}") 
        flag = flag+1
        multiply(num,flag)
multiply(num,flag)

# find out sum of digigts of the given number using functions type four 

number = input("enter your number : ")
value= [int(x) for x in number]
print(sum(value))




