import player
import dodeca
import item

house = dodeca.Dodeca()
player = player.Player(house.rooms[0])
baby_wumpus = item.Item("baby wumpus",20)

house.rooms[19].items.append(baby_wumpus)

