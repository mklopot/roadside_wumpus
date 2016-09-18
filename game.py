import random

import player
import dodeca
import item
#import wumpus
#import teleporter
import trapdoor

house = dodeca.Dodeca()
player = player.Player(house.rooms[0])
house.rooms[0].items.append(item.Item("blaster",2))
house.rooms[1].items.append(item.Item("charge cartridge",1))
house.rooms[1].items.append(item.Item("small artefact",1))

random.choice(house.rooms).items.append(item.Item("valuable artefact",20))
random.choice(house.rooms).items.append(item.Item("baby wumpus",40))

trapdoors = [trapdoor.Trapdoor(random.choice(house.rooms)),trapdoor.Trapdoor(random.choice(house.rooms))]
def post_player_action():
  if player.current_room in [trap.room for trap in trapdoors]:
    trapdoors[0].fall_thru(player,house.rooms[0],house.rooms)
  #wumpus.do_wumpus()
  #teleporter.do_teleporter()
  check_victory()

def check_victory():
  pass

 

