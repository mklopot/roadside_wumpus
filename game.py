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
player = player.Player(house.rooms[0])

indoors = [ room for room in house.rooms if not room is house.rooms[0] ]
random.choice(indoors).items.append(item.Item("blaster",5,"Well-made, but slightly rusty. Seems to be in good working order. Takes standard-issue cartridges."))
house.rooms[15].items.append(item.Item("charge cartridge",3,"Standard blaster cartridge: shaped like a laptop battery, but significantly heavier. This one is nearly all spent: the indicator shows just one charge left."))
random.choice(indoors).items.append(item.Item("small artefact",10,"A small black sphere, the size of a tennis ball, extremely heavy for its size. Once ins a while, of its own accord, lights up with different colors of the rainbow, and fades again."))

random.choice(indoors).items.append(item.Item("charge cartridge",3,"Standard blaster cartridge: shaped like a laptop battery, but significantly heavier. This one is nearly all spent: the indicator shows just one charge left."))
random.choice(indoors).items.append(item.Item("rainbow herring",2,"A pickled fish, with a characteristic smell. Probably about two pounds worth. Rainbow variety, the fattiest kind."))
random.choice(indoors).items.append(item.Item("brown herring",2,"A pickled fish, with a characteristic smell. Probably about two pounds worth. Brown variety, the cheapest kind."))
random.choice(indoors).items.append(item.Item("northern herring",2,"A pickled fish, with a characteristic smell.  Probably about two pounds worth. Northern variety, the mildest kind."))
random.choice(indoors).items.append(item.Item("red herring",2,"A pickled fish, with a characteristic smell. Red variety, the rarest kind, fo rthe true herring connoseur!"))
random.choice(indoors).items.append(item.Item("valuable artefact",80,"The artefact consists of two heavy round brass plates, interlocked together magnetically with about five inches between them. There is a thin layer of an unknown blue substance suspended in between the two plates"))
wumpus1 = wumpus.Wumpus(random.choice(indoors),house.rooms)
wumpus2 = wumpus.Wumpus(random.choice(indoors),house.rooms)
wumpuses = [wumpus1, wumpus2]

amulet_from_room = random.choice(indoors)
amulet1 = amulet.Amulet(amulet_from_room,random.choice(amulet_from_room.exits))

trapdoors = [trapdoor.Trapdoor(random.choice(indoors)),trapdoor.Trapdoor(random.choice(indoors))]
teleporters = [teleporter.Teleporter(random.choice(indoors),random.choice(indoors),indoors),teleporter.Teleporter(random.choice(indoors),random.choice(indoors),indoors)]

def status():
  for t in trapdoors:
    t.status(player)
  for t in teleporters:
    t.status(player)
  for w in wumpuses:
    w.status(player)
  player.status()

def post_player_action():
  for w in wumpuses:
    w(player)
  if player.current_room in [trap.room for trap in trapdoors]:
    trapdoors[0].fall_thru(player,random.choice(indoors),indoors)
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

