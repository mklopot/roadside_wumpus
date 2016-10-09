import sys
import random

class Cabbage():
  def __init__(self,current_room):
    self.name = "Devil's Cabbage"
    self.weight = 300
    self.description = "Something akin to a mutated fungus, the Devil's Spittin' Cabbage is a mottled sickly yellowish-green clump that spits deadly slime."
    self.current_room = current_room
    current_room.items.append(self)
  
  def status(self,player):
    if self.current_room in player.current_room.exits:
      print("You hear the rustling of a {} in an adjoining room.".format(self.name))
      
  def __call__(self,player):
    if self.current_room is None:
      return
    if player.current_room is self.current_room:
      print("There's a {} here!".format(self.name))
      if random.random() > .85:
        print("The {} spits deadly slime at you!".format(self.name))
        for item in player.inventory:
          if "bracelet" in item.name:
            item.save_life(player)
            return
        print("{} got you!".format(self.name))
        sys.exit(1)
      
