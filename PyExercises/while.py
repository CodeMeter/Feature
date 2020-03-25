card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand) < 17:
    hand.append(card_deck.pop())


# While Loop - Factorial of a number eg. 6! = 6*5*4*3*2*1=720
number = int(input("Enter to find a factorial of that number :"))
current = 1
product = 1
while current <= number:
    product *= current
    current += 1
print(product)


# For Loop - Factorial of a number eg. 6! = 6*5*4*3*2*1=720
number = int(input("Enter to find a factorial of that number :"))
current = 1
product = 1
for current in range(1, number+1):
    product *= current
    current += 1
print(product)

# Write a while loop that finds the largest square number less than an integer limit
# and stores it in a variable nearest_square

limit = 90
number = 0
while (number+1)**2 < limit:
    number += 1
    nearest_square = number**2
print(nearest_square)

# Write a loop that takes the numbers in a given list add up the odd numbers in the
# list but only up to the first 5 odd numbers together. If there are more than 5 odd
# numbers, you should stop at the fifth.If there are fewer than 5 odd numbers, add all of the odd numbers.
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542,
            87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
result = 0
count = 0
i = 0

while (count < 5) and (i < len(num_list)):
    print(num_list[i])
    if num_list[i] % 2 != 0:
        result += num_list[i]
        count += 1
    i += 1

print("The number of odd numbers are {}".format(count))
print("The sum of odd numbers are {}".format(result))

# Loading Items to ship with weight limit
manifest = [("bananas", 15), ("mattresses", 24),
            ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
i = 0
# write your loop here
while len(news_ticker) <= 140 and i <= len(headlines):
    news_ticker += headlines[i] + " "
    i += 1
    if len(news_ticker) > 140:
        slice_object = slice(140)
        news_ticker = (news_ticker[slice_object])
        break
print(news_ticker)


# Alternate Solution using for loop - Recommended solution
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)

# Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]
# write your code here
# HINT: You can use the modulo operator to find a factor
for number in check_prime:
    isPrime = True
    factor = ""
    for i in range(2, number):
        if (number % i) == 0:
            isPrime = False
            factor = factor + ',' + str(i)
            print(number)
            print(factor)

    if(isPrime):
        print('{} IS a prime number'.format(number))
    else:
        print('{} is NOT a prime number, because {} is a factor of {}'.format(
            number, factor, number))
        print(factor)

# Alternate way to find prime numbers from a list
check_prime = [26, 39, 51, 53, 57, 79, 85]

# iterate through the check_prime list
for num in check_prime:

    # search for factors, iterating through numbers ranging from 2 to the number itself
    for i in range(2, num):

        # number is not prime if modulo is 0
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(
                num, i, num))
            break

# otherwise keep checking until we've searched all possible factors, and then declare it prime
        if i == num - 1:
            print("{} IS a prime number".format(num))
