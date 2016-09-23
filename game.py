import random
import sys

import player
import dodeca
import item
import wumpus
import teleporter
import trapdoor

house = dodeca.Dodeca()
player = player.Player(house.rooms[0])
house.rooms[0].items.append(item.Item("blaster",2))
house.rooms[1].items.append(item.Item("charge cartridge",1))
house.rooms[1].items.append(item.Item("small artefact",1))

random.choice(house.rooms).items.append(item.Item("charge cartridge",1))
random.choice(house.rooms).items.append(item.Item("rainbow herring",1))
random.choice(house.rooms).items.append(item.Item("brown herring",1))
random.choice(house.rooms).items.append(item.Item("atlantic herring",1))
random.choice(house.rooms).items.append(item.Item("red herring",1))
random.choice(house.rooms).items.append(item.Item("valuable artefact",20))
wumpus1 = wumpus.Wumpus(random.choice(house.rooms),house.rooms)
wumpus2 = wumpus.Wumpus(random.choice(house.rooms),house.rooms)

trapdoors = [trapdoor.Trapdoor(random.choice(house.rooms)),trapdoor.Trapdoor(random.choice(house.rooms))]
teleporters = [teleporter.Teleporter(random.choice(house.rooms),random.choice(house.rooms),house.rooms),teleporter.Teleporter(random.choice(house.rooms),random.choice(house.rooms),house.rooms)]

def status():
  wumpus1.status(player)
  wumpus2.status(player)
  player.status()

def post_player_action():
  wumpus1(player)
  wumpus2(player)
  if player.current_room in [trap.room for trap in trapdoors]:
    trapdoors[0].fall_thru(player,random.choice(house.rooms),house.rooms)
  for t in teleporters:
    t(player)
  check_victory()

def check_victory():
  if wumpus1.current_room is None and wumpus2.current_room is None:
    print "You got both wumpuses!!"
    sys.exit()

 

