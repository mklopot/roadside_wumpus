import random
import sys

import player
import dodeca
import item
import wumpus
import teleporter
import trapdoor
import amulet
import cabbage
import safe
import buyer
import edible

house = dodeca.Dodeca()
player = player.Player(house.rooms[0])
buyer = buyer.Buyer(name="Dina the Buyer",description="Dina is middle-aged, disheveled, and dressed in paramilitary fatigues. She is carrying a metallic briefcase.")
house.rooms[0].items.append(buyer)

## The Courtyard and the Entryway should be clear of hazards, hazards can only be inside.
inside = [ room for room in house.rooms if not room is house.rooms[0] and not room is house.rooms[6]]

random.choice(inside).items.append(item.Item("blaster",10,"A well-made blaster, but slightly rusty. Seems to be in good working order. Takes standard-issue cartridges.",value=1700))
house.rooms[15].items.append(item.Item("blaster cartridge",3,"Standard blaster cartridge: shaped like a laptop battery, but significantly heavier. This one is nearly all spent: the indicator shows just one charge left.",value=10))
random.choice(inside).items.append(item.Item("'Black Droplet' artefact",10,"The artefact is a black spheroid, the size of a tennis ball, extremely heavy for its size. Once in a while, of its own accord, lights up with different colors of the rainbow, and fades again.",value=3000))
random.choice(inside).items.append(item.Item("'Black Droplet' artefact",10,"The artefact is a black spheroid, the size of a tennis ball, extremely heavy for its size. Once in a while, of its own accord, lights up with different colors of the rainbow, and fades again.",value=3000))
random.choice(inside).items.append(item.Item("'Black Droplet' artefact",10,"The artefact is a black spheroid, the size of a tennis ball, extremely heavy for its size. Once in a while, of its own accord, lights up with different colors of the rainbow, and fades again.",value=3000))

random.choice(inside).items.append(item.Item("blaster cartridge",3,"Standard blaster cartridge: shaped like a laptop battery, but much heavier. This one is nearly all spent: the indicator shows just one charge left.",value=10))
random.choice(inside).items.append(edible.Edible("rainbow herring",2,"A pickled fish, with a characteristic smell. Probably about two pounds worth. Rainbow variety, the fattiest kind.",value=3))
random.choice(inside).items.append(edible.Edible("brown herring",2,"A pickled fish, with a characteristic smell. Probably about two pounds worth. Brown variety, the cheapest kind.",value=3))
random.choice(inside).items.append(edible.Edible("northern herring",2,"A pickled fish, with a characteristic smell.  Probably about two pounds worth. Northern variety, the mildest kind.",value=3))
random.choice(inside).items.append(edible.Edible("red herring",2,"A pickled fish, with a characteristic smell. Red variety, the rarest kind, for the true herring connoseur!",value=3))
random.choice(inside).items.append(item.Item("'Witch's Wheel' artefact",95,"The artefact consists of two heavy round copper plates, interlocked together magnetically with about five inches between them. There is a thin layer of an unknown blue substance suspended between the two plates.",value=10000))

safe1 = safe.Safe(random.choice(inside))
blaster2 = item.Item("blaster",10,"A well-made blaster, in great condition. Seems to be in good working order. Takes standard-issue cartridges.",value=1900)
safe1.items.append(blaster2)
safe1.items.append(item.Item("blaster cartridge",3,"Standard blaster cartridge: shaped like a laptop battery, but much heavier. This one is nearly all spent: the indicator shows just one charge left.",value=10))
safe1.items.append(item.Item("blaster cartridge",3,"Standard blaster cartridge: shaped like a laptop battery, but much heavier. This one is nearly all spent: the indicator shows just one charge left.",value=10))

cabbage1 = cabbage.Cabbage(random.choice(inside))
cabbage2 = cabbage.Cabbage(random.choice(inside))
cabbages = [cabbage1,cabbage2]

wumpus1 = wumpus.Wumpus(random.choice(inside),inside)
wumpus2 = wumpus.Wumpus(random.choice(inside),inside)
wumpuses = [wumpus1, wumpus2]

amulet_from_room = random.choice(inside)
amulet1 = amulet.Amulet(amulet_from_room,random.choice(amulet_from_room.exits))

trapdoors = [trapdoor.Trapdoor(random.choice(inside)),trapdoor.Trapdoor(random.choice(inside))]
teleporters = [teleporter.Teleporter(random.choice(inside),random.choice(inside),inside),teleporter.Teleporter(random.choice(inside),random.choice(inside),inside)]

def status():
  for t in trapdoors:
    t.status(player)
  for t in teleporters:
    t.status(player)
  for c in cabbages:
    c.status(player)
  for w in wumpuses:
    w.status(player)
  player.status()

def post_player_action():
  for c in cabbages:
    c(player)
  for w in wumpuses:
    w(player)
  for t in teleporters:
    t(player)
  if player.current_room in [trap.room for trap in trapdoors]:
    trapdoors[0].fall_thru(player,random.choice(inside),inside)
  check_victory()

def passageway_hook(player,from_room,to_room):
  if from_room == amulet1.from_room and to_room == amulet1.to_room:
    amulet1(player)

def check_victory():
  if False not in [ w.current_room == None for w in wumpuses ]:
    print "You got all of the wumpuses!!"
    #sys.exit()

