# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, room):
    self.name = name
    self.room = room
    self.itembag = []

  def __repr__(self):
    return f"Player is in {self.room}"

  def pick_up(self, item):
    self.itembag.append(item)
