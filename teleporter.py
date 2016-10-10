import random

class Teleporter():
  def __init__(self,from_room,to_room, rooms):
    self.from_room = from_room
    self.to_room = to_room
    self.rooms = rooms

  def __call__(self,player):
    if player.current_room == self.to_room:
      print("The shadows in this room look strange.")
    if player.current_room == self.from_room:
      player.current_room = self.to_room
      print("The air shimmers unnaturally around you, your vision blurs, and you feel faint.\nAs you refocus your eyes, you find yourself TELEPORTED to a different room.")
      self.from_room = random.choice(list(set(self.from_room.exits).intersection(self.rooms)))
      self.to_room = random.choice(list(set(self.to_room.exits).intersection(self.rooms)))

  def status(self,player):
    if self.from_room in player.current_room.exits:
      print("You feel static electricity in the air, maybe there's a teleporter near.")

    
