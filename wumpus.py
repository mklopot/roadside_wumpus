import sys
import random

class Wumpus(object):
  def __init__(self,starting_room,habitat):
    self.name = "wumpus"
    self.weight = 300
    starting_room.items.append(self)
    self.habitat = habitat
    self.current_room = starting_room
    self.description = "This wumpus is a large, smelly, heavy creature with almost mollusk-like skin. The appendages (tentacles?) have suction cups. The sharp teeth are visible. It looks hungry!"
  
  def move_to(self,to_room,player):
    if to_room in self.current_room.exits:
      self.current_room.items.remove(self)
      self.current_room = to_room
      self.current_room.items.append(self)
      print("You hear {} footsteps in the distance.".format(self.name))
      if player.current_room is self.current_room:
        print("A menacing-looking {} prowls into the room!".format(self.name)) 

  def status(self,player):
    if self.current_room in player.current_room.exits:
      print("You smell a {} in an adjoining room.".format(self.name))

  def eat(self,food,player):
    if food in self.current_room.items:
      self.current_room.items.remove(food)
      self.weight += food.weight
      if self.current_room is player.current_room:
        print("The {} eats the {}.".format(self.name,food.name))
      else:
        print("You hear the {} eat a {} in the distance.".format(self.name,food.name))
         
      
  def __call__(self,player):
    if self.current_room is None:
      return
    for item in self.current_room.items:
      if type(item).__name__ is 'Edible':
        self.eat(item,player)
        return 
    if player.current_room is self.current_room:
      print("There's a {} here!".format(self.name))
      print("The {} pounces!".format(self.name))
      for item in player.inventory:
        if type(item).__name__ is "Amulet":
          item.save_life(player)
          return
      print("{} got you!".format(self.name.capitalize()))
      sys.exit(1)
    for room in self.current_room.exits:
      for name in [ item.name for item in room.items ]:
        if type(item).__name__ is 'Edible':
          self.move_to(room,player)
          return
    if random.random() >  .90:
      self.move_to(random.choice(self.current_room.exits),player)
      
