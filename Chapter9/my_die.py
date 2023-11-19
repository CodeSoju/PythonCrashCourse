from die import Die

my_die = Die()

for i in range(0, 10):
    print('Roll #', i+1, ':', my_die.roll_die())
    #print(my_die.roll_die())