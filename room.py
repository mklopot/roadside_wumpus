class Room:
    def __init__(self,exits,name,level=1):
	self.name = name
	self.exits = exits
        self.level = level
        self.items = []
