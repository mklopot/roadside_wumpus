import item

class Amulet(item.Item):
  def __init__(self,from_room,to_room):
    self.name = "gray metallic bracelet"
    self.weight = 1
    self.from_room = from_room
    self.to_room = to_room
    self.description = "A lot heavier than it looks, with very precise curvature, the gray metal seems to change shade depending on how the light falls on it. You have never seen anything quite like it!"

  def __call__(self,player):
    print("While going from the {} to the {}, you find a {}.\nYou like it so much, you put it on.".format(self.from_room.name,self.to_room.name,self.name))
    self.from_room = None
    self.to_room = None
    player.inventory.append(self)

  def save_life(self,player):
    print "Your life starts to flash befor eyour eyes.\n"
    print "Suddenly, time seems to freeze, and your {} crumbles to dust in slow motion.".format(self.name)
    print "It was an amulet of life-saving!"
    player.inventory.remove(self)
