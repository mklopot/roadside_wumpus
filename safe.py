import random

class Safe(object):
  def __init__(self,room,items=[]):
    self.name = "heavy safe"
    self.weight = 400
    self.items = items 
    self.room = room
    self.room.items.append(self)
    self.open = False
    self.description = "This is a heavy stainless steel safe, with a primitive electro-mechanical lock.\nIt looks like it will unlock, given the right combination."
    self.combo = random.randrange(0,99999)
     
  def unlock(self,player,input):
    if player.current_room is not self.room:
      print "There is no safe here to unlock."
      return
    if self.open == True:
      print "The safe is already open."
    else: 
      if input < self.combo:
        print "The mechanism makes a CLICK sound, but does not open." 
      elif input > self.combo:
        print "The mechanism makes a CLACK sound, but does not open." 
      else:
        self.open = True
        print "The safe opens!"
        if self.items:
          self.room.items.extend(self.items)
          print "Inside you find:"
          for item in self.items:
            print "      - {}".format(item.name)
          
