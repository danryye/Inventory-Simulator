import random
import pyinputplus as pyip

list_of_stuff = ['egg', 'apple', 'tomato', 'banana', 'orange', 'lemon']

my_inventory = {}
user_input = ''

def getitems():
    global my_inventory
    for count in range(0, random.randint(1,5)):
        item = list_of_stuff[random.randint(0, len(list_of_stuff)-1)]
        if item in my_inventory:
            my_inventory[item] += 1
        else:
            my_inventory.setdefault(item, 1)

while True:
    print('This is your current inventory: ')
    print(my_inventory)

    user_input = pyip.inputStr('type \'add\' to add items: ')

    if user_input == 'add':
        getitems()
    elif user_input == 'q' or user_input == 'quit':
        break
    else:
        print('Invalid input. Try again.')

print('Program finished. Goodbye.')



