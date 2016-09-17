import cmd
import gamestate

class repl(cmd.Cmd):
  def do_go(self,room_no):
#    try:
      gamestate.player.move_to(gamestate.player.current_room.exits[int(room_no)-1])
#    except:
#      print "No such room."

  def do_take(self,item_no):
    try:
      gamestate.player.take(gamestate.player.current_room.items[int(item_no)-1])
    except:
      print "No such item."

  def do_drop(self,item_no):
    try:
      gamestate.player.drop(gamestate.player.inventory[int(item_no)-1])
    except:
      print "No such item."

  def do_status(self, a):
    gamestate.player.status()

r = repl()
r.cmdloop()
