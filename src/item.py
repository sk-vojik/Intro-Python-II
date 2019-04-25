class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description
  
  def __repr__(self):
    return f"{self.name}"

class Food(Item):
  def __init__(self, name, description, calories):
    self.name = name
    self.description = description
    self.calories = calories
  def isFood(self):
    return true