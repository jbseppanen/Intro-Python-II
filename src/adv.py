from room import Room
from player import Player
from item import Item

# Declare all the rooms

rooms = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons."),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

# Create items
items = {
    'club': Item("Club", "A short chunk of an oak branch."),
    'shield': Item("Shield", "Dented and well used but still serviceable."),
    'sword': Item("Sword", "Sharp and in surprisingly good condition."),
    'matches': Item("Matches", "Dry and useable."),
    'coins': Item("Coins", "Just a few small ones missed by those who had been there before you.")
}

# Add Items to rooms

rooms['outside'].items.append(items['club'])
rooms['foyer'].items.append(items['shield'])
rooms['overlook'].items.append(items['sword'])
rooms['narrow'].items.append(items['matches'])
rooms['treasure'].items.append(items['coins'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
#
player = Player("George", rooms['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player.room.enter_room()

while True:
    user_input = input("What do you want to do here? ->")
    cmds = user_input.split(" ")
    if len(cmds) == 1:
        if user_input == "q":
            if input("Are you sure you want to quit? Enter y or n.") == "y":
                break
        if user_input == "n":
            if player.room.n_to is not None:
                player.room = player.room.n_to
                player.room.enter_room()
            else:
                print("Cannot go that direction.")
        elif user_input == "s":
            if player.room.s_to is not None:
                player.room = player.room.s_to
                player.room.enter_room()
            else:
                print("Cannot go that direction.")
        elif user_input == "e":
            if player.room.e_to is not None:
                player.room = player.room.e_to
                player.room.enter_room()
            else:
                print("Cannot go that direction.")
        elif user_input == "w":
            if player.room.w_to is not None:
                player.room = player.room.w_to
                player.room.enter_room()
            else:
                print("Cannot go that direction.")
        else:
            print("Unknown command.")
    elif len(cmds) == 2:
        if cmds[0].lower() == "get" or cmds[0] == "take" or cmds[0] == "pickup":
            player.pickup_item(items[cmds[1]])
        elif cmds[0].lower == "drop":
            player.drop_item(items[cmds[1]])
        else:
            print("Unknown command.")
    else:
        print("Unknown command.")

print("Exiting Game...")
