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
wumpuses = [wumpus1, wumpus2]

trapdoors = [trapdoor.Trapdoor(random.choice(house.rooms)),trapdoor.Trapdoor(random.choice(house.rooms))]
teleporters = [teleporter.Teleporter(random.choice(house.rooms),random.choice(house.rooms),house.rooms),teleporter.Teleporter(random.choice(house.rooms),random.choice(house.rooms),house.rooms)]

def status():
  for w in wumpuses:
    w.status(player)
  player.status()

def post_player_action():
  for w in wumpuses:
    w(player)
  if player.current_room in [trap.room for trap in trapdoors]:
    trapdoors[0].fall_thru(player,random.choice(house.rooms),house.rooms)
  for t in teleporters:
    t(player)
  check_victory()

def check_victory():
  if False not in [ w.current_room == None for w in wumpuses ]:
    print "You got all of the wumpuses!!"
    sys.exit()

 

