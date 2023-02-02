# comprehension for dictionaries

# old_recipes = {"biriyani":200,"panner butter masala" : 300, "sambar" : 100 }

# new_recipes = {item:price*2 for (item,price) in old_recipes.items()}
# print(new_recipes)

# #with conditions

# old_recipes = {"biriyani":200,"panner butter masala" : 300, "sambar" : 100 }

# new_recipes = {item:price*2 for (item,price) in old_recipes.items() if price<200}
# print(new_recipes)


# creating a list with eight customer names display a dictionary 
# which has customers names along with discounts for them from a particular shop 
# import random
# list = ["kishore","vamsi","shankar"]

# dict = {person:f"{random.randint(0,101)}%" for person in list}
# print(dict)

# creating dictionary from multiple lists using zip

# l1=['a','b','c']
# l2=[2,3,4]

# list_dict = {key:value for (key,value) in zip(l1,l2)}
# print(list_dict)



# create two lists first list should have five students name and in second list should contain their total marks 
# import random
# student_list = ["surya","yash","sendhil","roshan","paal"]
# dict = {name:f"{((random.randint(300,500))/500)*100}%" for name in student_list}
# print(dict)

# strings using backward slash
# h="hi i'am \"asdf\""
# print(h)


# string methods

# s="phaneendra   "
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.replace("ee","i"))
# print(s.strip())
# print(s.split("e"))
# print(s.center(20,"#"))
# print(s.strip())
# print(s.count("e"))
# print(s.count("a",4,len(s)))
# print(s.endswith(" ",0,len(s)))
# print(s.find("a",0,len(s)))
# print(s.index('a',1 ,len(s)))

# mutable and immutable concept
# mutable -can be changed
# immutable -can't be changed

# get one string as input along with a character find out and display whether that particular charcter present in the string 
# or not 

# be_string = input("enter the string:")
# character = input("enter your character:")
# print("character found") if(character in be_string) else print("not  found")


# check whether the given string is palindrome or not 

# beString = input("enter your value:")
# print(beString[::-1])
# print("yes it is palindrom") if beString== beString[::-1] else print("no its not")


# after getting one string as input check whether your string contains space or not if yes count no of spaces 

# beString = input("enter your string : ")
# print("space found") if (" " in beString) else print("not found")


#create list with vowels

str = input("enter your string : ")
vowels=["a","e","i","o","u","A","E","I","O","U"]
new = [i for i in str if i in vowels]
print(len(new))