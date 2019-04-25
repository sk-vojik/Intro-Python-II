# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, contains=0):
    self.name = name
    self.description = description
    self.contains = []
  
  def __repr__(self):
    return f"{self.name}, {self.description}"

  
  def add_item(self, item):
    self.contains.append(item)


