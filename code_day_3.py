







L= [1,4,7.4,"sam"]

print(L)
print(L[3])
print(L[2:3])
print(L[2:3])
print(L[0:])
print(L[:3])
print(L[-1])
print(L[::-1])

print(L)
L.append(4)
print(L)
L.extend([5,6])
print(L)
L.insert(1,22)
print(L)
L.remove(22)
print(L)
L.pop(3)
print(L)
L.clear()
print(L)
L= [1,4,7.4,1,1]
print(L)
L.index(7.4)
print(L)
L.count(1)
print(L)
L.sort()
print(L)
L.reverse()
print(L)



l = [1,2,3,2]

for i in range(len(l)):
    print(l[i])

for i in l :
    print(i)


for i in l :
    if (i%2==0):
        print(i)

l = int(input("enter your bloddy number:"))

def neonnum(l):
    numstr = str(l*l)
    sum =0
    for i in numstr:
        sum=sum+int(i)
    if(sum==l):
        print("it is neon")
    else:
        print("no its not")
        
neonnum(l)

# returning based on some condition

import math
list = list(map(int,input("enter value to be appended :").split()))
product= math.prod(list)
print(product if product<750 else sum(list))


numbers = [e for e in "Every day Eagle" if ord(e)>=65 and ord(e)<=90]
print(numbers)

set1 = {1,2,3,4,5,}
set2 = {6,7,8,1,2}
set1.add(10)
set1.discard(10)
print(set1 | set2)
print(set1 ^ set2)
print(set1 - set2)
print(set1.issuperset(set2))
print(set1.symmetric_difference(set2))


dictionary = {1:"one",2:"two","3" : [2,3]}
print(type(dictionary))
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

list = [1,2,3]
dictionary = dict()

for i in list:
     key = i
     value =int( input("inpurt evvara:"))
     dictionary.fromkeys(i,value)

print(dictionary)





