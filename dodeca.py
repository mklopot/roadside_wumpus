import room

class Dodeca(object):
  def __init__(self):
    self.room00 = room.Room([],"courtyard",1,"You are outside the oddly angular house. There is some mulched landscaping here, and an oak tree. A woman sits under the tree. She'll buy almost anything you can recover from the old building. Up a few steps there is a heavy door to the interior.")
    
    self.room01 = room.Room([],"basement",0,"The basement is musty and water-damaged. Rusty pipes run along the ceiling.")

    self.room02 = room.Room([self.room01],"cellar",0,"It's dark and damp here, and smells like old corks and maybe something like ether. There is a crunch of broken glass underfoot.") 
    self.room01.exits.append(self.room02)

    self.room03 = room.Room([self.room02],"subterranean room",0) 
    self.room02.exits.append(self.room03)

    self.room04 = room.Room([self.room03],"boiler room",0,"The walls here are lined with cinder blocks. The old boiler is rusted through, looks like it hasn't worked in ages. It makes hollow ringing noises from time to time.") 
    self.room03.exits.append(self.room04)

    self.room05 = room.Room([self.room04,self.room01],"understructure",0) 
    self.room04.exits.append(self.room05)
    self.room01.exits.append(self.room05)

    self.room06 = room.Room([self.room00,self.room01],"entryway",1,"The heavy door to the courtyard is shut, but a few rays of sunlight shine in. The hardwood floor creaks under your feet")
    self.room01.exits.append(self.room06)
    self.room00.exits.append(self.room06)

    self.room07 = room.Room([self.room06],"mezzanine",2,"The ceiing is low, and the white paint is peeling off the walls.") 
    self.room06.exits.append(self.room07)

    self.room08 = room.Room([self.room07,self.room02],"lobby",1,"The ornate woodwork is rotten, and the old flower pots have fallen over." ) 
    self.room07.exits.append(self.room08)
    self.room02.exits.append(self.room08)

    self.room09 = room.Room([self.room08],"library",2,"The walls are covered with bookshelves, floor to ceiling, but the dessicated old books crumble to dust as soon as you touch them.") 
    self.room08.exits.append(self.room09)

    self.room10 = room.Room([self.room09,self.room03],"antechamber",1) 
    self.room09.exits.append(self.room10)
    self.room03.exits.append(self.room10)
 
    self.room11 = room.Room([self.room10],"armory",2,"Only heavy cast iron hooks on the walls remain where enormous arcane laser rifles once hanged. A faint metallic smell is in the air.") 
    self.room10.exits.append(self.room11)

    self.room12 = room.Room([self.room11,self.room04],"vestibule",1) 
    self.room11.exits.append(self.room12)
    self.room04.exits.append(self.room12)
 
    self.room13 = room.Room([self.room12],"colonnade",2,"Bare white columns run up to the ceiling. An odd light fills this room.") 
    self.room12.exits.append(self.room13)

    self.room14 = room.Room([self.room13,self.room05],"foyer",1) 
    self.room13.exits.append(self.room14)
    self.room05.exits.append(self.room14)
 
    self.room15 = room.Room([self.room14,self.room06],"gallery",2) 
    self.room14.exits.append(self.room15)
    self.room06.exits.append(self.room15)
 
    self.room16 = room.Room([self.room07],"watchtower",3) 
    self.room07.exits.append(self.room16)

    self.room17 = room.Room([self.room16,self.room09],"alcove",3) 
    self.room16.exits.append(self.room17)
    self.room09.exits.append(self.room17)
 
    self.room18 = room.Room([self.room17,self.room11],"sky parlor",3) 
    self.room17.exits.append(self.room18)
    self.room11.exits.append(self.room18)

    self.room19 = room.Room([self.room18,self.room13],"attic",3) 
    self.room18.exits.append(self.room19)
    self.room13.exits.append(self.room19)
 
    self.room20 = room.Room([self.room19,self.room15,self.room16],"loft",3) 

    self.room19.exits.append(self.room20)
    self.room15.exits.append(self.room20)
    self.room16.exits.append(self.room20)

    self.rooms = [self.room00, self.room01, self.room02, self.room03, self.room04, self.room05, self.room06, self.room07, self.room08, self.room09, self.room10, self.room11, self.room12, self.room13, self.room14, self.room15, self.room16, self.room17, self.room18, self.room19, self.room20]

