#!/usr/bin/python

import cmd
import sys
import pickle

import game

class repl(cmd.Cmd):
  def do_go(self,room_no):
    try:
      game.player.move_to(game.player.current_room.exits[int(room_no)-1])
    except:
      print "No such room."
    game.post_player_action()
    game.status()

  def do_take(self,item_no):
    try:
      game.player.take(game.player.current_room.items[int(item_no)-1])
    except:
      print "No such item."
    game.post_player_action()
    game.status()

  def do_drop(self,item_no):
    try:
      game.player.drop(game.player.inventory[int(item_no)-1])
    except:
      print "No such item."
    game.post_player_action()
    game.status()


  def do_zap(self, item_no):
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

  def do_save(self, a):
    print("Saving your current game...")
    savefile = open("savefile", "wb")
    data = game.house, game.player, game.trapdoors, game.teleporters, game.wumpus1
    pickle.dump(data,savefile)
    savefile.close()
    print("Saved.")

  def do_load(self, a):
    print("Loading game from last save point...")
    try:
      savefile = open("savefile", "rb")
      game.house, game.player, game.trapdoors, game.teleporters, game.wumpus1 = pickle.load(savefile)    
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
r.cmdloop()
