
cities = ['Aa', 'Ba', 'Ca', 'Da', 'Ea']
capatilized_cities = []
for city in cities:
    print(city)
print("done")

for city in cities:
    capatilized_cities.append(city.upper())
    print(capatilized_cities)

# Indentation make the difference how they are printed
print(capatilized_cities)

# Create a new list out of existing list
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []
for name in names:
    usernames.append(name.lower().replace(" ", "_"))
print(usernames)

# Create a new list out of existing list using range function
usernames = ["Joy Tribbiani", "Mons Geller", "Chandan Bing", "Photo Buffay"]
for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ", "_")
print(usernames)


# Count the xml tags in a string
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if (token[0] == '<' and token[-1] == '>'):
        count += 1
print(count)

# Write an HTML code from given string
items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
# the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += '</ul>'
print(html_str)


# building dictionaries using for loop
book_title = ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes',
              'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']
word_counter = {}
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
print(word_counter)

# building dictionaries using get method
book_title1 = ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes',
               'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']
word_counter1 = {}

for word in book_title1:
    word_counter1[word] = word_counter1.get(word, 0) + 1
print(word_counter1)


# accessing dictionaries using for loop

cast = {
    "Jerry Seinfeld": "Jerry Seinfeld",
    "Julia Louis-Dreyfus": "Elaine Benes",
    "Jason Alexander": "George Costanza",
    "Michael Richards": "Cosmo Kramer"
}

# only access keys
for key in cast:
    print(key)

# access both keys and values
for key, value in cast.items():
    print("Actor : {}, Role : {}".format(key, value))

# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for object, count in basket_items.items():
    if object in fruits:
        result += count

print("There are {} fruits in the basket.".format(result))

# Only to get updated dictionaries
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through the dictionary
for fruit in basket_items:
    if fruit in fruits:
        basket_items[fruit] += 1
# if the key is in the list of fruits, add the value (number of fruits) to result

print(basket_items)
