class Room:
    def __init__(self,exits,name,level=1,description="You look around, and it generally looks exactly as you would expect."):
	self.name = name
	self.exits = exits
        self.level = level
        self.items = []
        self.description = description
