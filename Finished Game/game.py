#!/usr/bin/python3
import os
import sys
import random
from map import rooms
from player import *
from items import *
from gameparser import *



def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_buspass, item_id])
    'bus pass, id card'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_bottle, item_money, item_laptop])
    'bottle, money, laptop'

    """
    full = ""
    for item in items:
        full = full + item["name"] + ", "
    full = full[:-2]
    return(full)
    pass

def rand(difficulty):
    """
    
    >>> rand(0)
    True
    
    >>> rand(100)
    False
    
    """
    value = int(random.randrange(0, 101))
    ran = 100 - difficulty
    if value < ran or value == ran:
        win = True
    else:
        win = False
    return(win)    


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Lecture"])
    There is worksheet3 here.
    <BLANKLINE>

    >>> print_room_items(rooms["Kirill"])
    
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    items_in_room = ""
    for item in room["items"]:
        items_in_room = items_in_room + item["name"] + ", "
    items_in_room = items_in_room[:-2]
    if items_in_room == "":
        pass
    else:
        print("There is " + items_in_room + " here." + "\n")
    pass


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have laptop, money.
    <BLANKLINE>

    """
    inventory = list_of_items(items)
    if inventory == "":
        print("You have nothing in your inventory." + "\n")
    else:
         print("You have " + inventory + "." + "\n")


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

   
    >>> print_room(rooms["Bus"])
    <BLANKLINE>
    BUS
    <BLANKLINE>
    Bus Stop: You are at the bus stop. Your bus is already waiting.
    <BLANKLINE>

    >>> print_room(rooms["Kirill"])
    <BLANKLINE>
    KIRILL
    <BLANKLINE>
    You are in Kirill's Office, you see a range off high school muscial posters on the wall.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    print_room_items(room)
    

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:"""
    
    return(rooms[exits[direction]]["name"])


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    global complete
    global test_difficulty
    global sheet_1
    global sheet_2
    global sheet_3
    global assessments
    global complete
    global test_difficulty
    has_coffee = False
    
    for item in inventory:
        if item['name'] == 'coffee':
            has_coffee = True
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for item in room_items:
        print("TAKE " + item["id"] + " to take a " + item["name"])
    for item in inv_items:
        print("DROP " + item["id"] + " to drop your " + item["name"])
    for item in inv_items:
        if item["id"] == "worksheet1" and sheet_1 == False:
            print("COMPLETE Worksheet1")
        elif item["id"] == "worksheet2" and sheet_2 == False:
            print("COMPLETE Worksheet2")
        elif item["id"] == "worksheet3" and sheet_3 == False:
            print("COMPLETE Worksheet3")     
    if current_room["name"] == "SU":
        SU()
    elif current_room["name"] == "Window":
        print("FLY")
    elif current_room["name"] == "Transfer":
        transfer()
    elif current_room["name"] == "Lecture" and complete == False:
        lecture()
    elif current_room["name"] == "Home" and complete == True:
        print("SLEEP")
    elif current_room["name"] == "Kirill":
        a = False
        b = False
        c = False
        if assessments == 3 and sheet_1 == True and sheet_2 == True and sheet_3 == True:
            for item in room_items:
                if item["id"] == "worksheet1":
                    a = True
                elif item["id"] == "worksheet2":
                    b = True
                elif item["id"] == "worksheet3":
                    c = True
            if a == True and b == True and c == True:
                print("COMPLETE Course")
    if has_coffee == True:
        print("DRINK " + item_coffee['name'] + " to reduce your frustration by drinking coffee.")
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:
    """
    return chosen_exit in exits

def transfer():
    print("TRANSFER to Cardiff Metropolitan University")

def SU():
    global units
    print("DRINK Vodka")

def lecture():
    print("START Assessment")
        

def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the plagyer if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room
    pass_held = False
    id_held = False
    if move(current_room["exits"], direction) != "Cannot go that way":
        
        for item in inventory:
            if item['id'] == 'bus':
                pass_held = True
            elif item['id'] == 'id':
                id_held = True
        if pass_held == False and move(current_room['exits'], direction) == rooms['Bus']:
            print("You need your bus pass to ride the bus.")
            print("Press enter to continue")
            input("< ")
        elif id_held == False and move(current_room['exits'], direction) == rooms['University']:
            print("You need your Student ID to enter the University.")
            print("Press enter to continue")
            input("< ")
        else:
            current_room = move(current_room["exits"], direction)
            print("Moving to " + current_room["name"])
    else:
        print("You cannot go that way.")
        print("Press enter to continue")
        input("< ")


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    global current_room
    found = False
    for item in current_room["items"]:
        if item["id"] == item_id:
            inventory.append(item)
            current_room["items"].remove(item)
            found = True
    if found == False:
        print("You cannot take that.")
        print("Press enter to continue")
        input("< ")
        
    
    pass
    

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    global current_room
    found = False
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            current_room["items"].append(item)
            found = True
    if found == False:
        print("You cannot drop that.")
        print("Press enter to continue")
        input("< ")
        
    pass

def execute_drink(drink):
    """This function controls the drinking aspect of the game which you can use to control the frustration of your player, keeping the frustration below 100 is one of the goals of the game
    """
    global units
    global frustration
    if drink == 'vodka':
        units = units + 1
        frustration = frustration - 30
        if units > 3:
                print("You have had kidney failure and died from alcohol poisoning, on the bright side you don't have to hand in your assessment tomorrow!")
                print("Press enter to exit")
                input("< ")
                sys.exit("")
    elif drink == 'coffee':
        frustration = frustration - 10
        inventory.remove(item_coffee)
        print("Somehow, that was both disgusting and amazing... But at least you feel less frustrated now!")
        rooms['Cafeteria']['items'].append(item_coffee)
    else:
        print("Drink what?")
        print("Press enter to continue")
        input("< ")
        
 
def execute_transfer(place):
    if place == "cardiff":
        print("You have transferred to Cardiff Met. Congratulations you have completed your degree in poor decision making")
        print("Press enter to exit")
        input("< ")
        sys.exit("")
    else:
        print("Transfer where?")

def execute_complete(sheet):
    global sheet_1
    global sheet_2
    global sheet_3
    global assessments
    global frustration
    if sheet == "worksheet1":
        for item in inventory:
            if item["id"] == sheet:
                frustration = frustration + 25
                sheet_1 = True
    elif sheet == "worksheet2":
        for item in inventory:
            if item["id"] == sheet:
                frustration = frustration + 25
                sheet_2 = True
    elif sheet == "worksheet3":
        for item in inventory:
            if item["id"] == sheet:
                frustration = frustration + 25
                sheet_3 = True
    elif sheet == "course":
        a = False
        b = False
        c = False
        if assessments == 3 and sheet_1 == True and sheet_2 == True and sheet_3 == True:
            for item in room_items:
                if item["id"] == "worksheet1":
                    a = True
                elif item["id"] == "worksheet2":
                    b = True
                elif item["id"] == "worksheet3":
                    c = True
            if a == True and b == True and c == True:
                print("Congratulations you have completed your course!!!")
                print("Press enter to exit")
                sys.exit("")
    else:
        print("Complete What?")
        print("Press enter to continue")
        input("< ")
        
def exam(difficulty):
    global test_difficulty
    global test_active
    test_active = True
    print("You can:")
    print("ATTEMPT test({}% success rate)".format(str(100 - difficulty)))
    print("CHEAT(50% success rate)")
    print("LEAVE(0% success rate)")
    print("COUGH")
    print("What do you want to do?")
    user_input = input("> ")
    normalised_user_input = normalise_input(user_input)
    test_difficulty = difficulty
    execute_command(normalised_user_input)   
    
def execute_exam(test):
    global complete
    global fail
    global test_difficulty
    global assessments
    if assessments == 0:
        while complete == False:
            os.system('cls')
            print("You sit down and stare at the exam paper in front of you:")
            print("CM1011 EXAM -  CuTe CaTz")
            print("Example Question:")
            print("Q: How many programmers does it take to change a light bulb?")
            print("A: None, thats a hardware problem")
            print("After reading the paper you start to wonder why you thought it was a good idea  to watch TV instead of revising last night")
            print("You look up from the paper, hoping to see someone that appears to be as confused as you are so that you feel better about yourself")
            test_difficulty = 25
            exam(test_difficulty)
    elif assessments == 1:
        while complete == False:
            os.system('cls')
            print("You sit down and stare at the exam paper in front of you:")
            print("CM1012 EXAM - My Favourite Poem - Kirill")
            print("Example Question:")
            print("Q: Why don't jokes work in octal?")
            print("A: Because 7 10 11")
            print("Roses are red")
            print("My USB stick is blue")
            print("I love computers")
            print("You should too")
            print("You look up from the paper")
            test_difficulty = 50
            exam(test_difficulty)
    elif assessments == 2:
        while complete == False:
            os.system('cls')
            print("You sit down and stare at the exam paper in front of you:")
            print("CM1013 EXAM - Hustlin'")
            print("Example Question:")
            print("Q: What is required to understand recursion?")
            print("A: You must first understand recursion")
            print("*Photo of Kirill Hustlin'*")
            test_difficulty = 75
            exam(test_difficulty)
        pass

    
    
def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    global complete
    global test_pass
    global assessments
    global frustration
    global test_active
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")
            print("Press enter to continue")
            input("< ")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")
            print("Press enter to continue")
            input("< ")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
            print("Press enter to continue")
            input("< ")
            
    elif command[0] == "drink":
        if len(command) > 1 :
            execute_drink(command[1])
        else:
            print("Take what?")
            
    elif command[0] == "transfer":
        if len(command) > 1:
         if current_room["name"] == "Transfer":
            execute_transfer(command[1])
         else:
            print("You can only transfer in the transfer hub")

    elif command[0] == "start":
         if current_room["name"] == "Lecture" and complete == False:
             if len(command) > 1:
                 execute_exam(command[1])
             else:
                 print("start what?")
                 print("Press enter to continue")
                 input("< ")
    elif command[0] == "cough":
        if current_room["name"] == "Lecture" and test_active == True:
            print("Someone coughs in reply")
            print("Press enter to continue")
            input("> ")
        else:
            print("Everyone knows that you can only cough in an exam")
            print("Press enter to continue")
            input("> ")
    elif command[0] == "attempt":
        if current_room["name"] == "Lecture" and test_active == True:
            complete = True
            assessments = assessments + 1
            test_pass = rand(test_difficulty)
            if test_pass == True:
                print("Congratulations! Some how you managed to pass the test")
                print("Press enter to continue")
                input("> ")
                frustration = frustration - 30
            elif test_pass == False:
                print("Unlucky! You failed the test")
                print("Press enter to continue")
                input("> ")
                frustration = frustration + 50
            test_active = False
        else:
            print("Attempt what?")
            print("Press enter to continue")
            input("> ")
    elif command[0] == "cheat":
        if current_room["name"] == "Lecture" and test_active == True:
            complete = True
            assessments = assessments + 1
            caught = rand(25)
            test_pass = rand(50)
            if caught == False:
                print("You get caught cheating and get kicked out of the course. Nice job...")
                print("Press enter to exit")
                sys.exit("")
            if test_pass == True:
                print("Congratulations! Thanks to the person next to you, you passed the test")
                print("Press enter to continue")
                input("> ")
                frustration = frustration - 30
            elif test_pass == False:
                print("Unlucky! You successfully managed to cheat but shouldn't have copied as you still failed the test")
                print("Press enter to continue")
                input("> ")
                frustration = frustration + 50
            test_active = False
        else:
            print("What you mean cheat?")
            print("Press enter to continue")
            input("> ")
    elif command[0] == "leave":
        if current_room["name"] == "Lecture" and test_active == True:
            complete = True
            assessments = assessments + 1
            print("You realise that you really don't care what you get in this test and walk out")
            print("Press enter to continue")
            input("> ")
            frustration = frustration + 40
            test_active = False
        else:
            print("You have no exam to walk out off...")
            print("Press enter to continue")
            input("> ")
    elif command[0] == "sleep":
        if current_room["name"] == "Home" and complete == True:
                    complete = False
                    print("You dream once again about the idea of Wales winning the Rugby World Cup...")
                    print("You wake up and realise how ridiculous your dream was")
                    print("Press enter to continue")
                    input("> ")    
                    frustration = frustration - 10
        else:
            print("You can't sleep here")
    elif command[0] == "complete":
        if len(command) > 1:
            execute_complete(command[1])
        else:
            print("complete what?")
            print("Press enter to continue")
            input("< ")
    elif command[0] == 'fly':
        if current_room['name'] == 'Window' and random.randint(0,100) <= 10:
            print("You successfully fly away from Cardiff University! We don't know how, but clearly there's a bug in real life ")
            print("Press enter to exit")
            input("< ")
            sys.exit("")
        elif current_room['name'] == 'Window':
            print("Unfortunately (yet not surprisingly), you've not managed to fly with just your arms - how shocking")
            print("Press enter to exit")
            input("< ")
            sys.exit("")
    else:
        print("This makes no sense.")
        print("Press enter to continue")
        input("< ")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """
    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return(normalised_user_input)
    
def check_frustration():
    global frustration
    if frustration < 0:
        frustration = 0
    print("Your frustration is " + str(frustration) + ".")
    if frustration >= 100:
        print("You have become too frustrated and died from stress")
        print("Press enter to continue")
        input("> ")
        sys.exit("")
        
    


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Kirill"]["exits"], "south") == rooms["University"]
    True
    >>> move(rooms["Transfer"]["exits"], "north") == rooms["Cafeteria"]
    True
    >>> move(rooms["Lab"]["exits"], "west") == rooms["Kirill"]
    False
    """

    # Next room to go to
    if is_valid_exit(exits, direction) == True:
        return(rooms[exits[direction]])
    else:
        return "Cannot go that way"
# This is the entry point of our program
def main():
    global has_won
    global units
    global assessments
    global complete
    global test_pass
    global test_difficulty
    global sheet_1
    global sheet_2
    global sheet_3
    global frustration
    global test_active
    print("""
 _____ _             _       _     _      
/  ___| |           (_)     | |   | |     
\ `--.| |_ _ __ __ _ _  __ _| |__ | |_    
 `--. \ __| '__/ _` | |/ _` | '_ \| __|   
/\__/ / |_| | | (_| | | (_| | | | | |_    
\____/ \__|_|  \__,_|_|\__, |_| |_|\__|   
                        __/ |             
                       |___/              
 _____       _   _                        
|  _  |     | | | |                       
| | | |_   _| |_| |_ __ _                 
| | | | | | | __| __/ _` |                
\ \_/ / |_| | |_| || (_| |                
 \___/ \__,_|\__|\__\__,_|                                                          
  ____                       _____      _ 
/  __ \                     /  ___|    (_)
| /  \/ ___  _ __ ___  _ __ \ `--.  ___ _ 
| |    / _ \| '_ ` _ \| '_ \ `--. \/ __| |
| \__/\ (_) | | | | | | |_) /\__/ / (__| |
 \____/\___/|_| |_| |_| .__/\____/ \___|_|
                      | |                 
                      |_| 
Press Enter To Begin...
""") 
    input("> ")
    test_difficulty = 0
    frustration = 0
    test_pass = False
    complete = False
    sheet_1 = False
    sheet_2 = False
    sheet_3 = False
    test_active = False
    units = 0
    assessments = 0
    has_won = False
    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        os.system('cls')
        check_frustration()
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

