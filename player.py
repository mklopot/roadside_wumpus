class Player(object):
    def __init__(self, current_room):
        self.current_room = current_room
        self.last_room = None
        self.inventory = []
        self.max_carry_weight = 100
        self.currency = 0
        self.destroyed = []

    def move_to(self, to_room):
        if to_room in self.current_room.exits:
            up_down = ""
            if self.current_room.level > to_room.level:
              up_down = "down "
            elif self.current_room.level < to_room.level:
              up_down = "up "
            self.last_room = self.current_room
	    self.current_room = to_room
            print("You go {}to the {}.".format(up_down,self.current_room.name))
            if not self in self.current_room.seen_by:
              print self.current_room.description
              print
              self.current_room.seen_by.append(self)
        else:
            print("There is no way to go to the "+to_room.name+".")

    def take(self, item):
        if type(item).__name__ == "Buyer":
          print "You decide against it."
          return
        if item in self.current_room.items:
            if sum(i.weight for i in self.inventory) + item.weight <= self.max_carry_weight:
                self.current_room.items.remove(item)
                self.inventory.append(item) 
            elif item.weight > self.max_carry_weight:
                print(item.name.capitalize()+" is too heavy to carry.")
            else:
                print(item.name.capitalize()+" is too heavy to carry right now.")
        else:
            print("The "+item.name+" is not here.")

    def drop(self, item):
        if item in self.inventory:
                self.current_room.items.append(item)
                self.inventory.remove(item) 
        else:
            print("You do not have "+item.name+".")

    def zap(self,target):
      if type(target).__name__ == "Buyer":
        print "You decide against it."
        return
      if "blaster" in [ item.name for item in self.inventory ]:
        if "blaster cartridge" in [ item.name for item in self.inventory ]:
          if target in self.current_room.items:
            self.current_room.items.remove(target)
            self.destroyed.append(target)
            for item in self.inventory:
              if item.name == "blaster cartridge":
                self.inventory.remove(item)
                break
            print("*** ZAP!! The {} disintegrates into a million pieces!!! ***\n".format(target.name))
            if type(target).__name__ in ["Wumpus","Cabbage"] :
              target.current_room = None 
          else:
            print("That target is not here.")
        else:
          print("A blaster charge cartridge is needed to fire the blaster.")
      else:
        print("There is no blaster in your inventory.")
            

    def status(self):
        print("You are in the "+self.current_room.name+".")

        if self.current_room.exits:
            i = 1
            print("From here, you can go to the:")
            for exit in self.current_room.exits:
                print("    {}. {}".format(i,exit.name))
                i += 1
        else:
            print("You see no exits from this place.")

        if self.inventory:
            i = 1
            print "You have:"
            for item in self.inventory:
                print("    {}. {}".format(i,item.name))
                i += 1
        else:
            print("You have no items in your posession.")
 
        if self.current_room.items:
            i = 1
            print("You see here:")
            for item in self.current_room.items:
                print("    {}. {}".format(i,item.name))
                i += 1

    def score(self):
      if self.currency:
        print("You have made ${}.".format(self.currency))
      if self.destroyed:
        print "You managed to destroy:"
        for item in self.destroyed:
          print " - {}".format(item.name)

       
    def sell(self,item,buyer):
      if buyer not in self.current_room.items:
        print "The buyer is not here."
      else:
        response= raw_input("{} offers ${} for the {}. Accept? (y/n) ".format(buyer.name,item.value,item.name))
        if response.lower()[0] is "y":
          self.inventory.remove(item)
          self.currency += item.value
          print("You now have a total of ${}.".format(self.currency))
        else:
          print "You decline the offer."
      
        

