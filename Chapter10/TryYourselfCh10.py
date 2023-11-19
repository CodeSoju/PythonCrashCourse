'''
10-1 Learning Python: Open a blank file in your text editor and write a few lines summarizing
what you've leanred about Python so far. 
Start each line with the phrase In Python you can... 
Save the file as learning_python.txt in the same directory
'''
'''
filename = 'learning_python.txt'

with open(filename) as file_object: 
    lines = file_object.readlines()

file_content = ''

for line in lines: 
    line = line.replace('object', "VroomVroom")
    file_content += line.rstrip()

print(file_content)
'''

'''
10-2: Learning C
You can use the replace() method to replace any word in a string with a different
word. Here's a quick example showing how to replace 'dog' with 'cat' in a sentence: 
'''
'''
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

    file_content = ''

    for line in lines:
        line = line.replace('Python', 'C')
        file_content += line.rstrip(' ')
    
    print(file_content)
'''
'''
10-3. Guest
Write a program that prompts the user for their name. When they respond write their name
to a file called guest.txt
'''
'''
filename = 'guest_list.txt'
switch = True

with open(filename, 'w') as file_object:
    file_object.write( "Names of guests:\n ")
    file_object.write('--------------------\n')

while switch:
    guest_name = input('\nPlease enter your name: ')

    with open(filename, 'a') as file_object:
        file_object.write(guest_name + '\n')
    
    response = input('Would you like to quit program? (Y/N):')
    if response == 'Y':
        switch = False
    elif response == 'N':
        continue

    
print(file_object)
'''

'''
10-4. Guest Book:
Write a while loop that prompts users for their name. When they enter their name, 
print a greeting to the screen and add a line recording their vit in a file
called guest_book.txt. Make sure each entry appears on a new line in the file. 
'''
'''
filename = 'guest_book.txt'
switch = True

with open(filename, 'w') as file_object:
    file_object.write( "Guest Book:\n ")
    file_object.write('--------------------\n')

while switch:
    guest_name = input('\nPlease enter your name: ')

    with open(filename, 'a') as file_object:
        print(f'Welcome {guest_name} to Hotel Sparrow! \nWe hope you will enjoy your stay!')
        file_object.write(guest_name + 'is occupying a room.\n')
    
    response = input('Would you like to quit program? (Y/N):')
    if response == 'Y':
        switch = False
    elif response == 'N':
        continue

    
print(file_object)
'''

'''
10-6 Addition
One common problem when prompting for a numerical input occurs when people provide
text instead of numbers. When you try to convert the input to an int, you'll get a 
ValueError. Write a program that prompts for two numbers. Add them together and print 
the result. Catch the ValueError if either input value is not a number, and print a 
friendly error message. Test your program by entering two numbers and then by entering 
some text instead of a number. 
'''
'''
def addition(firstNum, secondNum):
    return firstNum + secondNum

print("********ADDITION CALCULATOR********")
print("Please input two numbers to add together\n")

while True:
    try:
        number_one = int(input("First Number: "))
        number_two = int(input("Second Number: "))
        print(addition(number_one, number_two))
    except ValueError:
        print("The input isn't a number.")
    answer = input("Do you wish to continue? (Y/N): ")
    if answer == 'Y':
        continue
    elif answer == 'N':
        break
'''

'''
10-8 Cats and Dogs:
Make two files, cat.txt and dogs.txt. Store ar least three names of cats in the first file
and three names of dogs in the second file. Write a program that tries to read these files
and print contents of the file to the screen. 
Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message
if a file is missing. Move one of the files to a different location on your system, and make sure the code
in the except block executes properly. 
'''
'''
filenames= ['cats.txt', 'dogs.txt', 'horses.txt']
try:
    for filename in filenames:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
            print(contents + '\n')
except FileNotFoundError:
    pass
'''

'''
10-10 Common Words:
Use the count() method to find out how many times a word or phrase appears in a string. 
'''

'''
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        print(f'Looking at {filename}\n')
        word = input('Insert a word that you\'d like to count the instances of: ')
        words = contents.split()
        #word_count = words.lower().count(word)
        word_count = 0
        for w in words:
            if w == word:
                word_count += 1
        
        print(f"The word '{word}' appears {word_count} times.\n")

filenames = ['alice.txt', 'Flatland.txt', 'siddhartha.txt', 'MobyDick.txt', 'TheHoundOfTheBaskervilles.txt']
for filename in filenames:
    count_words(filename)
'''

'''
10-11 Favorite Number:
Write a program that prompts for the user's favorite number. Use json.dump() to store this number
in a file. Write a separate program that reads in this value and prints the message. "I know your favorite number!
It's _____"
'''
'''
import json

def get_number():
    try:
        fav_num = int(input('What is your favorite number? '))
        filename = 'fav_num.json'
    except ValueError:
        print("The value inputted isn't an int. Please try again.")
    else:
        with open(filename, 'w') as f:
            json.dump(fav_num, f)
    return fav_num

def read_num():
    filename = 'fav_num.json'
    try:
        with open(filename) as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        print(f"I know your favorite number. It's {fav_num}.")

def favorite_number():
    favorite_number = read_num()
    if favorite_number:
        print(f"You're favorite number is {favorite_number}")
    else:
        favorite_number = get_number()
        print(f"Your favorite number is {favorite_number}!")

favorite_number()
'''

'''
10-13 Verify User:
The final listing for remember_me.py assumes either that the user has already entered their username
or that the program is running for the first time. We should modify it in case the current user is not the persom who last used the program. 
Before printing a welcome back message in greet_user(), ask the user if this is the correct username. 
If it's not, call get_new_username() to get the correct username. 

'''

