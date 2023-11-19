filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

'''
The blank line appears b/c read() returns an empty string when it reaches the end of
the file; this empty string shows up as a blank line. If you want to remove the extra blank
line, you can use rstrip() in the call to print(). 

rstrip() method removes, or strips, any whitespace characters from the right side of a string. 
Now the output matches the contents of the original file exactly.

FILE PATHS
-----------
A relaticve path tells Python to look for a given location relative to the directory where the currently
running program file is stored. 

readlines() method takes each line from the file and stores it in a list. This list is then 
assigned to lines, which we can continue to work w/ after the with block ends. 
'''


'''
Writing to a File:

Writing to an Empty File: 
    To write text to a file, you need to call open() iwht a 2nd arg telling Python that yo
    want to write to the file. 

    filename = 'Programminf.txt' 

    with opne(filename, 'w') as file_object:
        file_name.write("I love programmin")

tThe 'w' tells python you want to open the file in write mode. 
'''