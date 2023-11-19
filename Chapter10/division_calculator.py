print('Input two numbers to divide.')
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second Number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

'''
The only code that should go in a try block is code that might cause an exception to be raised. 
Sometimes you'll have additional code that should run only if the try block was successful; 
this code goes in the else block. The except block tells Python what to do in case a certain
exception arises when it tries to run the code in the try block. 

HANDLING THE FileNotFoundError Exception:
----------------------------------------
One common issue when working with files is handling missing files. The file you're looking
for might be in a different location, the filename may be misspelled, or the file may not 
exist at all. You can handle all of these situations in a straightforward way with a try-except
block. 

look at alice.py
'''
