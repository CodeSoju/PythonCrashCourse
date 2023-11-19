'''
WRITING T0 A FILE
-------------------
When you write to a file, the output will still be avilable after you close the terminal
containing your program's output. 

Writing to an Empty File:
-------------------------
To write text to a file, you need to call open() with a second argument telling
Python that you want to write to the file. 
'''

filename = 'programming.txt'

'''
with open(filename, 'w') as file_object:
    file_object.write("This is all mundane.")
'''

'''
The call to open() in this example has two arguments. The first argument is still the name
of the file we want to open. The 2nd arg, 'w' tells Python that we want to open the file
in 'write mode'. 

You can open a file in 'read mode' ('r'), write mode ('w'), append mode ('a'), or a mode
that allows you to read and write to the file ('r+'). 
If you omit the mode arg, Python opens the file in read-only mode by default. 

The open() function automatically creates the file you're writing to if it doesn't already exist. 
However, be careful opening a file in write mode ('w') b/c if the file does exist, Python
will erase the contents of the file before returning the file object. 


WRITING MULTIPLE LINES:
------------------------
The write() function doesn't add any newlines to the text we write. So if you write
more than one line without including newline characters, your file may not look the way you 
want it to:


APPENDING TO A FILE:
-------------------
If you want to add content to a file instead of writing over exisiting content, 
you can open the file in append mode. When you open a file in append mode, 
Python doesn't erase the contents of the file before returning the file object. 
'''

with open(filename, 'a') as file_object:
    file_object.write("The sun explodes into tiny fragements that \n")
    file_object.write("will nourish the surronding stars within the galaxy.\n")