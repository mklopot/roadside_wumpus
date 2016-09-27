import random

class Trapdoor():
  def __init__(self,room):
    self.room = room

  def fall_thru(self,player,fall_to,items_to):
    player.current_room = fall_to
    print("A TRAP DOOR opens under you, you fall down to a different room, and hit the ground with a THUD...")
    if player.inventory:
      print("Your items fell out somewhere along the way.")
      for item in player.inventory:
        print("Lost "+item.name)
        random.choice(items_to).items.append(item) 
      player.inventory = []
