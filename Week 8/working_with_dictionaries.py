#creating a dictionary
pizza_prefs = {}

pizza_prefs['name'] = "sandeep"
pizza_prefs['toppings'] = "mushrooms"

print(pizza_prefs)

pizza_prefs = {'name': 'sandeep', 'toppings': 'mushrooms'}

print(pizza_prefs)

pizza_prefs = [{'name': 'sandeep', 'toppings': 'mushrooms', 'pizza_type': 'round'},
               {'name': 'kylie', 'toppings': ['ham', 'pineapple'], 'pizza_type': 'square'},
               {'name': 'lisa', 'toppings': ['mushrooms', 'pepperoni'], 'pizza_type': 'square'},
               {'name': 'dan', 'toppings': ['sausage', 'bacon', 'pepperoni'], 'pizza_type': 'square'}]


#simple user search
for person in pizza_prefs:
    if person['name'] == "sandeep":
        print(person['toppings'])
    else:
        print("This is not sandeep")

#complex search
for person in pizza_prefs:

    mushrooms_found = False

    if type(person['toppings']) is str:
        if(person['toppings']) == "mushrooms":
            mushrooms_found = True
    elif type(person['toppings']) is list:
        if("mushrooms" in person['toppings']):
            mushrooms_found = True
    
    if mushrooms_found:
        print(person['name'] + " likes mushrooms")

#removing value from list
print(pizza_prefs)

for person in pizza_prefs:

    mushrooms_found = False

    if type(person['toppings']) is str:
        if(person['toppings']) == "mushrooms":
            mushrooms_found = True
    elif type(person['toppings']) is list:
        if("mushrooms" in person['toppings']):
            mushrooms_found = True
    
    if mushrooms_found:
        pizza_prefs.remove(person)

print(pizza_prefs)