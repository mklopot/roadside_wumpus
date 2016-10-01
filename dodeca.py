import room

class Dodeca():
  def __init__(self):
    self.room01 = room.Room([],"entryway",0)

    self.room02 = room.Room([self.room01],"foyer",0) 
    self.room01.exits.append(self.room02)

    self.room03 = room.Room([self.room02],"lobby",0) 
    self.room02.exits.append(self.room03)

    self.room04 = room.Room([self.room03],"antechamber",0) 
    self.room03.exits.append(self.room04)

    self.room05 = room.Room([self.room04,self.room01],"vestibule",0) 
    self.room04.exits.append(self.room05)
    self.room01.exits.append(self.room05)

    self.room06 = room.Room([self.room01],"diamond room",1)
    self.room01.exits.append(self.room06)

    self.room07 = room.Room([self.room06],"emerald room",1) 
    self.room06.exits.append(self.room07)

    self.room08 = room.Room([self.room07,self.room02],"amber room",1) 
    self.room07.exits.append(self.room08)
    self.room02.exits.append(self.room08)

    self.room09 = room.Room([self.room08],"marble room",1) 
    self.room08.exits.append(self.room09)

    self.room10 = room.Room([self.room09,self.room03],"malachite room",1) 
    self.room09.exits.append(self.room10)
    self.room03.exits.append(self.room10)
 
    self.room11 = room.Room([self.room10],"ruby room",2) 
    self.room10.exits.append(self.room11)

    self.room12 = room.Room([self.room11,self.room04],"gold room",2) 
    self.room11.exits.append(self.room12)
    self.room04.exits.append(self.room12)
 
    self.room13 = room.Room([self.room12],"silver room",2) 
    self.room12.exits.append(self.room13)

    self.room14 = room.Room([self.room13,self.room05],"iridium room",2) 
    self.room13.exits.append(self.room14)
    self.room05.exits.append(self.room14)
 
    self.room15 = room.Room([self.room14,self.room06],"bronze room",2) 
    self.room14.exits.append(self.room15)
    self.room06.exits.append(self.room15)
 
    self.room16 = room.Room([self.room07],"red room",3) 
    self.room07.exits.append(self.room16)

    self.room17 = room.Room([self.room16,self.room09],"yellow room",3) 
    self.room16.exits.append(self.room17)
    self.room09.exits.append(self.room17)
 
    self.room18 = room.Room([self.room17,self.room11],"blue room",3) 
    self.room17.exits.append(self.room18)
    self.room11.exits.append(self.room18)

    self.room19 = room.Room([self.room18,self.room13],"green room",3) 
    self.room18.exits.append(self.room19)
    self.room13.exits.append(self.room19)
 
    self.room20 = room.Room([self.room19,self.room15,self.room16],"indigo room",3) 
    self.room19.exits.append(self.room20)
    self.room15.exits.append(self.room20)
    self.room16.exits.append(self.room20)

    self.rooms = [self.room01, self.room02, self.room03, self.room04, self.room05, self.room06, self.room07, self.room08, self.room09, self.room10, self.room11, self.room12, self.room13, self.room14, self.room15, self.room16, self.room17, self.room18, self.room19, self.room20]

