import random

class Safe():
  def __init__(self,items=[]):
    self.weight = 400
    self.items = items 
    self.open = False
    self.description = "A heavy stainless steel combination safe. Enter the combination to open."
    self.combo = random.randrange(0,99999)
     
  def open(self,input):
    if self.open = True:
      print "The safe is already open."
    else: 
      if input < self.combo:
        print "The blue light comes on." 
      elif input > self.combo:
        print "The orange light comes on." 
      else:
        self.open = True
        print "The safe opens!"
        if safe.items:
          print "Inside you find:"
          for item in safe.items:
            print "- {}".format(item.name)
          
