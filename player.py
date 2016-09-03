class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory = []
        self.max_carry_weight = 100

    def move_to(self, to_room):
        if to_room in self.current_room.exits:
	    self.current_room = to_room
            print("You go to the "+self.current_room.name+".")
        else:
            print("There is no way to go to the "+to_room.name+".")

    def take(self, item):
        if item in self.current_room.items:
            if sum(i.weight for i in self.inventory) + item.weight <= self.max_carry_weight:
                self.current_room.items.remove(item)
                self.inventory.append(item) 
            else:
                print(item.name+" is too heavy to carry right now.")
        else:
            print("The "+item.name+" is not here.")

    def drop(self, item):
        if item in self.inventory
                self.current_room.items.append(item)
                self.inventory.remove(item) 
        else:
            print("You do not have "+item.name+".")

    def status(self):
        print("You are in the "+self.current_room.name+". You feel great!")

        if self.current_room.exits:
            for exit in self.current_room.exits:
                print("You can go to the "+exit.name+" from here.")
        else:
            print("You see no exits from this place.")

        if self.inventory:
            print "You have:"
            for item in self.inventory:
                print item.name
                print
        else:
            print("You have nothing in your posession")

        if self.current_room.items:
            print("You see here:")
            for item in self.current_room.items:
                print(item.name)
       
