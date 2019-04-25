from room import Room
from player import Player
from item import Item, Food

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

rock = Item("Rock", "This is a rock")
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("scott", room['outside'])
# print(player)
print(player)

def try_direction(direction, room):
  attribute = direction + "_to"

  # See if the inputted direction is one we can move to
  if hasattr(room, attribute):
    #fetch the new room
    return getattr(room, attribute)
  else:
    print("The path is blocked - try a different way")
    return room

# Write a loop that:
while True:
# * Prints the current room name

  print(f"You are at: {player.room.name}")



# * Prints the current description (the textwrap module might be useful here).
  print(f"Description: {player.room.description}")
# * Waits for user input and decides what to do.
  s = input("\n>").lower().split()

  print(s)

  if len(s) == 1:
    #user passed us a direction

      # grab the first character of the first word
      s = s[0][0]
    if s == "q":
      print("Adios!")
      break
    player.set_current_room(try_direction(s, player.room))
    

    player.room = try_direction(s, player.room)
  elif len(s) == 2:
    #user passed two word
    first_word = s[0]
    second_word = s[1]

    if first_word
  else:
    print("I didn't get that - please try again")
    continue

 
  # if s == "n":
  #   player.room = player.room.n_to
  # elif s == "s":
  #   player.room = player.room.s_to
  # elif s == "e":
  #   player.room = player.room.e_to
  # elif s == "w":
  #   player.room = player.room.w_to
  # else:
  #   print("Not a valid direction!")
#
# If the user enters a cardinal direction, attempt to move to the room there.


# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
