#Problem 6-1
#Stores information about a favorite movie within a dictionary
print("Problem 6-1: ")

favorite_movie = {'movie_title': 'Shawshank Redemption', 'rating': '9.3/10', 'director': 'Frank Darabont', 'year_released': '1994', 'writer': 'Stephen King', 
                   'production_company': 'Castle Rock Entertainment'}

#Problem 6-2
#Stores information about a product in a dictionary, raises price by 30%, then prints a statement that the price of that product increased
print("\nProblem 6-2: ")

product_info = {'item_number': '978-1593279288', 'product_name': 'Python Crash Course', 'price': '21.24'}

product_info['price'] = float(product_info['price']) * 1.3

print("The price of " + product_info['product_name'] + " has increased by 30%" + " and now costs " + str(product_info['price']))

#Problem 6-3
#Prints the contents of the list in problem 6-1 
print("\nProblem 6-3: ")

for value in favorite_movie:
    print(value.title() + ": " + str(favorite_movie[value]))

#Problem 6-4
#Creates a list of dictionary terms and prints each one using a loop
print("\nProblem 6-4: ")

dictionary_items = [{'word': 'item', 'definition': 'an individual article or unit, especially one that is part of a list, collection, or set.'}, 
                    {'word': 'create', 'definition': 'bring (something) into existence.'},
                    {'word': 'list', 'definition': 'a number of connected items or names written or printed consecutively, typically one below the other.'}]

for word in dictionary_items:
    print(word['word'].title() + ": " + word['definition'])

#Problem 6-5
#Adds another key to the dictionary in problem 6-1 containing the cast of the movie, then loops through the cast and prints each name
print("\nProblem 6-5: ")

favorite_movie = {'movie_title': 'Shawshank Redemption', 'rating': '9.3/10', 'director': 'Frank Darabont', 'year_released': '1994', 'writer': 'Stephen King', 
                   'production_company': 'Castle Rock Entertainment', 'cast': ['Tim Robbins', 'Morgan Freeman', 'Bob Gunton', 'William Sadler']}

for name in favorite_movie['cast']:
    print(name)