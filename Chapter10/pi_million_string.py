filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string: 
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi!")

'''
Python has no inherent limit to how much data you can work with; you can work with as much
data as your system's memory can handle. 
'''

'''
Is your birthday contained in Pi?
Let's use the program we jsut wrote to find out if someone's Bday appears anywhere in the first million
digits of pi. 
We can do this by expressing each birthday as a string of digits and seeing if the string appears anywhere in pi_string: 
'''