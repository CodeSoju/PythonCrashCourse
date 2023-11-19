'''
Python uses special objects called exceptions to manage errors that arise during
a program's execution. 
Whenever an error occurs that makes Python unsure what to do next, it creates an exception
object. If you wirte code that handles the exception, the program will continue running. 
If you don't handle the exception the program will halt and show a 'traceback'
which includes a report of the exception that was raised. 

try-except blocks
'''
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

'''
If the code in the try block causes an error, Python looks for an except block whose error 
matches the one that was raised and runs the code in that block

Using Expceptions to Prevent Crashes
------------------------------------
look at division_calculator.py


The else Block:
----------------
looks at alice.py

WORKING WITH MULTIPLE FILES
---------------------------
LOOK AT word_count.py

Now we can write a simple loop to count the words in ahy text we want to analyze. 
We do this by storing the names of the files we want to analyze in a list, and then 
we call count_words for each file in the list. 

Using the try-except block in this example provides two significant advatnages. We prevent our users from 
seeing a traceback, and we let the program continue analyzing the texts it's able to find. If
we don't catch the FileNotFoundError that siddahartha.txt raised, the user would see a 
full traceback, and the program would sop running after trying to analyze Siddartha. It would
never analyze Moby Dick. 

Failing Silently:
------------------
pass statement also acts as a placeholder. It's a reminder that you're choosing to do nothing
at a specific point in your program's execution and that you might want to do something
there later. For example, in this program we might decide to write any missing filenames 
to a file called missing_files.txt. Other users wouldn't see this file, but we'd be able to read
the file and deal with any missing texts. 

DECIDING WHICH ERRORS TO REPORT:
--------------------------------
Giving users information they aren't looking for can decrease the usability of your
program. Python's error-handling structures give you fine-grained control over how much
to share with users when things go wrong; it's up to you to decide how much information
to share. 


STORING DATA:
-------------
The json module allows you to dump simple Python data structures into a file and load
the data from that file the next time the program runs. You can also use json to share 
data between diffeent Python programs. 

Using json.dump() and json.load():
-----------------------------------
The first program will use json.dump() to store the set of numbers, and the second program
will use jon.load()

The json.dump() function takes two arguments: a piece of data to sore and a file object
it can use to store the data. 

Now we'll write a program that uses json.load() to read the list back into memory:
looks at number_reader.py

SAVING AND READING USER-GENERATED DATA:
-----------------------------------------
look at remember_me.py


REFACTORING:
-------------
Often, you'll come to a point where your code will work, but you'll recognize that you could 
improve the code by breaking it up into a series of functions that have specific jobs. 
This process is called refactoring. Refactoring makes your code cleaner, easier to
understand, and easier to extend. 

We can refactor remember_me.py by moving the bulk of its logic into one or more functions. 
The focus of remember_me.py is on greeting the user, so let's move all of our exisiting code
intp a function called greet_user():

A function should either return the value you're expecting, or it should return None. This allows
us to perform a simple test with the reuturn value of the function
'''