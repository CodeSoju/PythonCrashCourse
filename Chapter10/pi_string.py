filename = 'pi_digits.txt'

#readlies() method takes each line from the file and stores it in a list. 
#This list is then assigned to lines, which we can continue to work with after the with block
#ends. 
with open(filename) as file_object:
    lines = file_object.read()

print(lines)
#pi_string = ''
#for line in lines:
 #   pi_string += line.rstrip()

#print(pi_string)
#print(len(pi_string))

'''
When Python reads from a text file, it interprets all text in the file as a string. 
If you read in a number and want to work with that value in a mumerical context, you'll
have to convert it to an interger using the int() function or convert it to a float
using the float() function
'''

'''
Large FIles: One Million Digits
-----------

'''