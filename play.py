#!/usr/bin/python

import cmd
import sys
import difflib
import pickle

import game

class repl(cmd.Cmd):
  def do_go(self,room_description):
    try:
      room_no = int(room_description) - 1
    except:
      room_description = difflib.get_close_matches(room_description, [room.name for room in game.player.current_room.exits],1,.4)
      if room_description:
        room_no = [room.name for room in game.player.current_room.exits].index(room_description[0]) 
      else:
        print("Instructions unclear.")
        return
    try:
      game.player.move_to(game.player.current_room.exits[int(room_no)])
    except:
      print "No such room."
    game.post_player_action()
    game.status()

  def do_take(self,item_description):
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
    game.post_player_action()
    game.status()

  def do_drop(self,item_description):
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
    game.post_player_action()
    game.status()


  def do_zap(self, item_description):
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
      game.player.zap(game.player.current_room.items[int(item_no)-1])
    except: 
      print "No such target."
    game.post_player_action()
    game.status()
   

  def do_status(self, a):
    game.status()

  def do_wait(self, a):
    print("You wait for a few moments.")
    game.post_player_action()

  def do_exit(self, a):
    print
    print "Bye!"
    sys.exit()

  def do_quit(self, a):
    print
    print "Bye!"
    sys.exit()

  def do_save(self, a):
    print("Saving your current game...")
    savefile = open("savefile", "wb")
    data = game.house, game.player, game.trapdoors, game.teleporters, game.wumpuses
    pickle.dump(data,savefile)
    savefile.close()
    print("Saved.")

  def do_load(self, a):
    print("Loading game from last save point...")
    try:
      savefile = open("savefile", "rb")
      game.house, game.player, game.trapdoors, game.teleporters, game.wumpuses = pickle.load(savefile)    
    except:
      print("Could not load game state from file...")
    else:
      print("Loaded.")
    finally:
      savefile.close()
    game.status()

  do_EOF = do_exit

  def preloop(self):
    game.status()

r = repl()
r.prompt = "\n> "
print
print "Welcome to Roadside Wumpus!"
print
print "Commands are:"
print "    go   take   drop   zap   wait   status   save/load"
print 
print "Refer to rooms and items by their number, or name."
print "For example:"
print "> go 1         or          > take 3"
print "or:"
print "> go to the vestibule      >take blaster"
print 
print "Hazards are: teleporters, trap doors, and TWO wumpuses!"
print
r.cmdloop()
