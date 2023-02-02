# comprehension for dictionaries

old_recipes = {"biriyani":200,"panner butter masala" : 300, "sambar" : 100 }

new_recipes = {item:price*2 for (item,price) in old_recipes.items()}
print(new_recipes)

#with conditions

old_recipes = {"biriyani":200,"panner butter masala" : 300, "sambar" : 100 }

new_recipes = {item:price*2 for (item,price) in old_recipes.items() if price<200}
print(new_recipes)


