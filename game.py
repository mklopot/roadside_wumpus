import random
import sys

import player
import dodeca
import item
import wumpus
import teleporter
import trapdoor
import amulet

house = dodeca.Dodeca()
player = player.Player(house.rooms[5])
random.choice(house.rooms[10].exits).items.append(item.Item("blaster",5))
house.rooms[15].items.append(item.Item("charge cartridge",3))
random.choice(house.rooms).items.append(item.Item("small artefact",10))

random.choice(house.rooms).items.append(item.Item("charge cartridge",3))
random.choice(house.rooms).items.append(item.Item("rainbow herring",2))
random.choice(house.rooms).items.append(item.Item("brown herring",2))
random.choice(house.rooms).items.append(item.Item("northern herring",2))
random.choice(house.rooms).items.append(item.Item("red herring",2))
random.choice(house.rooms).items.append(item.Item("valuable artefact",80))
wumpus1 = wumpus.Wumpus(random.choice(house.rooms),house.rooms)
wumpus2 = wumpus.Wumpus(random.choice(house.rooms),house.rooms)
wumpuses = [wumpus1, wumpus2]

amulet_from_room = random.choice(house.rooms)
amulet1 = amulet.Amulet(amulet_from_room,random.choice(amulet_from_room.exits))

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

def passageway_hook(player,from_room,to_room):
  if from_room == amulet1.from_room and to_room == amulet1.to_room:
    amulet1(player)

def check_victory():
  if False not in [ w.current_room == None for w in wumpuses ]:
    print "You got all of the wumpuses!!"
    sys.exit()

