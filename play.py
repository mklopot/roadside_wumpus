import cmd
import sys
import game

class repl(cmd.Cmd):
  def do_go(self,room_no):
#    try:
      game.player.move_to(game.player.current_room.exits[int(room_no)-1])
#    except:
#      print "No such room."
      game.player.status()

  def do_take(self,item_no):
    try:
      game.player.take(game.player.current_room.items[int(item_no)-1])
    except:
      print "No such item."
    game.player.status()

  def do_drop(self,item_no):
    try:
      game.player.drop(game.player.inventory[int(item_no)-1])
    except:
      print "No such item."
    game.player.status()


  def do_zap(self, item_no):
#    try:
      game.player.zap(game.player.current_room.items[int(item_no)-1])
#    except: 
#      print "No such target."
   

  def do_status(self, a):
    game.player.status()

  def do_exit(self, a):
    print "Bye!"
    sys.exit()

  def preloop(self):
    game.player.status()

r = repl()
r.prompt = "\n> "
print
print "Welcome to Roadside Wumpus!"
print
r.cmdloop()
