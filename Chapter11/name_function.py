def get_formatted_name(first, last, middle=''):
    ''' generate a neatly formatted full name. '''
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

'''To check that get_formatted_name() works, let's make a program that uses 
this function. Look at names.py, which will let users enter a fisrt and last name, and
see a neatly formatted full name'''