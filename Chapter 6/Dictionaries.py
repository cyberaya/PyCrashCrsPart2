# nl() = new_line()
def nl():
    print('\n')


print('This chapter is on Dictionaries!\n')
# Below you see the alien's 'attributes', AKA key-value pairs, assigned in the given dictionary.
# Pretty self explanatory, its color is green and is worth 5 points.
alien_0 = {'color': 'green', 'points': 5}

# The lines below print out the two key-value pairs on separate lines.
print((alien_0['color']))
print(alien_0['points'])

nl()
# A dictionary in Python is a collection of key-value pairs.
# Each key is connected to a value, and you can use a key to access the value associated with that key.
# A key’s value can be a number, a string, a list, or even another dictionary.
# A key-value pair is a set of values associated with each other.
# When you provide a key, Python returns the value associated with that key.
# Every key is connected to its value by a colon, and individual key-value pairs are separated by commas.
# You can store as many key-value pairs as you want in a dictionary.

# To get the value associated with a key,name of the dictionary (alien_0),then place the key [color]in square brackets.
print(alien_0['color'])
nl()
# Below, we assign our 'points' key value (in the dictionary alien_0) to the variable new_points.
new_points = alien_0['points']
print(f'You just earned {new_points} points!')

# Dictionaries are dynamic and can be assigned new key value pairs.
# Below we are adding x and y positions to the dictionary alien_0 as key pairs.
alien_0['x_position'] = 0
alien_0['y_position'] = 25
# By printing alien_0 now, we will return 4 key-pairs instead of 2.
print(alien_0)

# It’s sometimes convenient, or even necessary, to start with an empty dictionary and then add each new item to it.
# For example:

# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)

nl()

# Modifying values in a dictionary:
alien_two = {'color': 'green'}
print(f"The alien is {alien_two['color']}.")

alien_two['color'] = 'yellow'
print(f"The alien is now {alien_two['color']}.")

nl()

# This is extra credit of me using my information as an example in a dictionary.
angel_raya = {'age': 27, 'years': 'decade'}
print(f"His name is Angel and he is {angel_raya['age']} years old.")

# angel_raya['age'] = '29'
# print(f"Two years have since passed and Angel Raya is now {angel_raya['age']} years old.")

if angel_raya['years'] == 'decade':
    age_increment = 10
elif angel_raya['years'] == 'twenty':
    age_increment = 20
else:
    print('Unknown age!')

angel_raya['age'] = angel_raya['age'] + age_increment

print(f"A decade has passed and Angel is now {angel_raya['age']}, or 10 years older.")

nl()

# Notice in the dictionary below the integers do not have '' around them.
# x position starts at 0, and y commences at 25, the third key-pair 'speed' is assigned the value 'medium'.
alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_1['x_position']}")

# Now move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien!
    x_increment = 3

# The new position is the old position plus the increment.
# Think of what is happening here, x_position is essentially appending + x_increment from if elif else statement.
# By doing this, x_position (beginning at 0) is now at position 2 because the speed == 'medium' (increments in 2)
alien_1['x_position'] = alien_1['x_position'] + x_increment

print(f"New position: {alien_1['x_position']}")

# Use the below line of code to add the speed 'fast' to the dictionary.
alien_1['speed'] = 'fast'

# In order for the code to work properly and add the increment of 3, we must reuse the if, elif, else statement.
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien!
    x_increment = 3

# We will now add to the y position instead.
alien_1['y_position'] = alien_1['y_position'] + x_increment

# The code should now execute an increment of 3 because I added [speed] = 'fast' and reused if,elif,else.
print(f"Position after adding 'fast speed' to y_position: {alien_1['y_position']}")
nl()


# Removing key-value pairs
# When you no longer need a piece of info stored in a dictionary, you can use the del statement to remove a key pair.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

nl()

# A Dictionary of Similar Objects
fave_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
# Create a new variable - language - and assign the dictionary - fave_languages with the key value of ('jen')
# This will call Jen's fave programming language only, and of course we use - .title() - to upper case python.
language = fave_languages['jen'].title()
print(f"Jen's favorite language is {language}.")


sarah = fave_languages['sarah'].title()
print(f"Sarah's favorite programming language is {sarah}, and Edward's is {fave_languages['edward'].title()}.")

language2 = fave_languages['jen'].title()
print(f"Both Jen's and Phil's go-to language is {language2}")
nl()

# Using get() to Access Values
# Using keys in square brackets to retrieve the value you’re interested in from a dictionary might cause one problem:
# If the key you ask for doesn’t exist, you’ll get an error.

# For dictionaries,you can use the get() method to set a default value that will be returned if the requested key
# doesn’t exist. The get() method requires a key as a first argument. As a second optional argument, you can pass the
# value to be returned if the key doesn’t exist:

illegal_alien = {'color': 'green', 'speed': 'slow'}

point_value = illegal_alien.get('points', 'No point value assigned')
print(point_value)

# If there’s a chance the key you’re asking for might not exist, consider using the get() method instead of the square
# bracket notation.

# Remember, you can append to the dictionary like so:
illegal_alien['points'] = 15
# Now you can print the value of points.
print(illegal_alien['points'])
nl()

# EXERCISES!

# Exercise 1
shannon_mae = {'fName': 'shannon', 'l_Name': 'roberts', 'age': 22, 'city': 'chicago'}
print(shannon_mae)
print(shannon_mae['fName'].title())
print(shannon_mae['l_Name'].title())
print(shannon_mae['age'])
print(shannon_mae['city'].title())
nl()

print('This exercise below displays coworkers and their favorite numbers.')

# Exercise 2
coworkers = {
    'ht': 79,
    'lr': 26,
    'dw': 12,
    'ar': 75,
    }

coworkers2 = coworkers['ht']
coworkers3 = coworkers['lr']
coworkers4 = coworkers['dw']
coworkers5 = coworkers['ar']

nl()

print(f"My coworker HT says his favorite number is {coworkers2}.")
nl()
print(f"My coworker LR says his favorite number is {coworkers3}.")
nl()
print(f"My coworker DW previously told me his number of choice is {coworkers4}.")
nl()
print(f"The homie AR stated he like the number {coworkers5}.")
nl()
# Exercise 3
glossary = {'tuples': 'a list of items that cannot be changed.',
            'string': 'a series of characters inside quotes.',
            'list': 'a collection of items in a particular order.',
            'dictionary': 'a collection of key-value pairs.',
            }
print('Below you can find a short glossary of different Python programming keywords.\n')
print(f"tuple:\n".title() + f"Is {glossary['tuples']}")
nl()
print(f"String:\nIs {glossary['string']}")
nl()
print(f"List:\nIs {glossary['list']}")
nl()
print(f"Dictionary:\nIs {glossary['dictionary']}")


