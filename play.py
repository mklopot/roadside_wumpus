#!/usr/bin/python

import cmd
import sys
import difflib
import pickle
import code
import re

import game

class repl(cmd.Cmd):
  def do_debug(self,a):
    banner = """
*********************
 Debug the Wumpus!
Interactive Console 
  Ctrl-D to exit
*********************"""
    code.interact(banner=banner,local=globals())
    game.status()

  def do_1(self,a):
    self.do_go("1")

  def do_2(self,a):
    self.do_go("2")

  def do_3(self,a):
    self.do_go("3")

  def do_4(self,a):
    self.do_go("4")

  def do_back(self,a):
    self.do_go("back")

  def do_go(self,room_description):
    try:
      room_no = int(room_description) - 1
    except:
      if room_description == "back" and game.player.last_room in game.player.current_room.exits:
        room_description = game.player.last_room.name
      else:
        room_description = difflib.get_close_matches(room_description, [room.name for room in game.player.current_room.exits],1,.4)
        if room_description:
          room_description = room_description[0]
      if room_description:
        room_no = [room.name for room in game.player.current_room.exits].index(room_description) 
      else:
        print("Instructions unclear.")
        return
    try:
      game.player.move_to(game.player.current_room.exits[int(room_no)])
    except:
      print "No such room."
      return
    game.passageway_hook(game.player,game.player.last_room,game.player.current_room)
    game.post_player_action()
    game.status()

  def do_take(self,item_description):
    if len(game.player.current_room.items) == 1:
      item_no = 0
    else:
      try:
        item_no = int(item_description) - 1
      except:
        item_description = difflib.get_close_matches(item_description, [item.name for item in game.player.current_room.items],1,.4)
        if item_description:
          item_no = [item.name for item in game.player.current_room.items].index(item_description[0]) 
        else:
          print("Instructions unclear.")
          return
    try:
      game.player.take(game.player.current_room.items[int(item_no)])
    except:
      print "No such item."
      return
    game.post_player_action()
    game.status()

  def do_drop(self,item_description):
    if len(game.player.inventory) == 1:
      item_no = 0
    else:
      try:
        item_no = int(item_description) - 1
      except:
        item_description = difflib.get_close_matches(item_description, [item.name for item in game.player.inventory],1,.4)
        if item_description:
          item_no = [item.name for item in game.player.inventory].index(item_description[0]) 
        else:
          print("Instructions unclear.")
          return
    try:
      game.player.drop(game.player.inventory[int(item_no)])
    except:
      print "No such item."
      return
    game.post_player_action()
    game.status()


  def do_zap(self, item_description):
    if len(game.player.current_room.items) == 1:
      item_no = 0
    else:
      try:
        item_no = int(item_description) - 1
      except:
        item_description = difflib.get_close_matches(item_description, [item.name for item in game.player.current_room.items],1,.4)
        if item_description:
          item_no = [item.name for item in game.player.current_room.items].index(item_description[0]) 
        else:
          print("Instructions unclear.")
          return
    try:
      game.player.zap(game.player.current_room.items[int(item_no)])
    except: 
      print "No such target."
      return
    game.post_player_action()
    game.status()
   
  def do_look(self,item):
    if item == "" or item == "around":
      print game.player.current_room.description
      return
    else:
      try:
        item_no = int(item) - 1
        if len(game.player.current_room.items + game.player.inventory) <= item_no:
          print("Instructions unclear")
          return
      except:
        item_description = difflib.get_close_matches(item, [item.name for item in game.player.current_room.items + game.player.inventory],1,.4)
        if item_description:
          item_no = [item.name for item in game.player.current_room.items + game.player.inventory].index(item_description[0])
        else:
          print("Instructions unclear.")
          return
    print (game.player.current_room.items + game.player.inventory)[item_no].description

  def do_sell(self,item_description):
    if len(game.player.inventory) == 1:
      item_no = 0
    else:
      try:
        item_no = int(item_description) - 1
      except:
        item_description = difflib.get_close_matches(item_description, [item.name for item in game.player.inventory],1,.4)
        if item_description:
          item_no = [item.name for item in game.player.inventory].index(item_description[0])
        else:
          print("Instructions unclear.")
          return
    game.player.sell(game.player.inventory[int(item_no)],game.buyer)
    game.post_player_action()
    game.status() 

  def do_unlock(self,combo):
    combo = re.findall("\d+",combo) 
    if combo:
      combo = max(combo)
    for item in game.player.current_room.items:
      if "safe" in item.name:
        if combo == []:
          combo = raw_input("Enter combination: ")
        try:
          combo = int(combo)
        except:
          print "Combination must be numeric." 
          return
        item.unlock(game.player,int(combo))
        game.post_player_action()
        game.status() 
        return
    print "There is no safe here to unlock."

  def do_status(self, a):
    game.status()

  def do_wait(self, a):
    print("You wait for a few moments.")
    game.post_player_action()
    game.status()

  def do_exit(self, a):
    print
    if game.player.currency > 0:
      print "You made ${}.".format(game.player.currency)
    if game.player.destroyed:
      print "You managed to destroy:"
      for item in game.player.destroyed:
        print " - {}".format(item.name)
    print "Bye!"
    sys.exit()

  do_quit = do_exit

  do_EOF = do_exit

  def do_save(self, a):
    print("Saving your current game...")
    savefile = open("savefile", "wb")
    data = game.house, game.player, game.trapdoors, game.teleporters, game.wumpuses, game.amulet1, game.buyer, game.cabbages, game.safe1
    pickle.dump(data,savefile)
    savefile.close()
    print("Saved.")

  def do_load(self, a):
    print("Loading game from last save point...")
    try:
      savefile = open("savefile", "rb")
      game.house, game.player, game.trapdoors, game.teleporters, game.wumpuses, game.amulet1, game.buyer, game.cabbages, game.safe1 = pickle.load(savefile)    
    except:
      print("Could not load game state from file...")
    else:
      print("Loaded.")
    finally:
      savefile.close()
    game.status()

  def preloop(self):
    game.status()

r = repl()
r.prompt = "\n> "
print
print "Welcome to Roadside Wumpus!"
print
print "Commands are:"
print "    go   take   drop   zap   look   wait   unlock   status   save/load"
print 
print "Refer to rooms and items by their number, or name."
print "For example:"
print "> go 1         or          > take 3"
print "or:"
print "> go to the vestibule      > take blaster"
print "_______________________________________________________________"
print 
print 
print "You are in a courtyard, next to an old building with odd angles."
print "There is a woman here. She is Dina the Buyer."
print
print "She says, 'PSST! I buy any old junk you can salvage from this weird house."
print "The more rare and interesting, the better! Oh, and there are wumpuses inside."
print "Some folks like to hunt 'em!"
print "Watch out for: teleporters, trap doors, Devil's Cabbage, and TWO wumpuses!'"
print
r.cmdloop()
