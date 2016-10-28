class Room(object):
    def __init__(self,exits,name,level=1,description="You look around, and the surroundings generally look pretty much as you would expect for a {}."):
	self.name = name
	self.exits = exits
        self.level = level
        self.items = []
        self.description = description.format(name)
        self.seen_by = []
