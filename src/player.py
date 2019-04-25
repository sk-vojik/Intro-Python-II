# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, room):
    self.name = name
    self.room = room
    self.itembag = []
    self.strength = 0

  def __repr__(self):
    return f"Player is in {self.room}"

  def pick_up(self, item):
    self.itembag.append(item)
  
  def set_current_room(self, new_room):
    self.room = new_room

  def printInventory(self):
    for item in self.items:
      print(item)
  def eat(self, item):
    if item.isFood() and item in self.items:
      print(f"You have eaten {item.name}")
      self.items.remove(item)
      self.strength += item.calories
    else:
      print("You cannot eat that")
