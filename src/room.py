# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, contains):
    self.name = name
    self.description = description
    self.contains = []

  
  def add_item(self, item):
    self.contains.append(item)
