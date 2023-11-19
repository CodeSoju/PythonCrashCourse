'''
9-14: Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select
four numbers or letters from the list and print a message saying that any ticket matching these four numbers
or letters wins a prize
'''
from random import randint

lottery_choices = ['A', 'B', 'C', 'D', 'E', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
winning_ticket = 'C2A9'

bought_ticket = []

counter = 0

def generate_ticket():
    for i in range(0, 4):
        bought_ticket.append(lottery_choices[randint(0, len(lottery_choices) - 1)])
        print(''.join(bought_ticket))


while True:
    generate_ticket()

    if ''.join(bought_ticket) != winning_ticket:
        print("Not a winning ticket!")
        counter += 1
        bought_ticket.clear()
    else:
        break

print('Winning Ticket: ', ''.join(bought_ticket))
print(f'It only took  {counter} times')

'''
STYLING CLASSES
--------------
Classes names should be written in CamelCase. Instance and module names should be written in lowercase
w/ underscored between words. 
Every class should have a dcostring immediately following the class defintion. The docstring description
should be about what the class does, and you should follow the same formatting conventions you used for writing docstrings
in functions. Each module should also have a docstring describing what the classes in a module can be used for. 
'''