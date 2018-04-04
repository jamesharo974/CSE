class Room(object):
    def __init__(self, name, description, north, south, east, west, up, down):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


playground = Room("Playground", "You are at the playground.", 'garage', 'shed', 'lake', 'tower', None, None)
garage = Room("Garage", "The car is not here.", 'master', 'playground', None, None, None, None)
master = Room("Master Bedroom", "You just entered the house. Wow what a big room.", 'bedroom', 'garage', None, 'bathroom', None, None)
bedroom = Room("Bedroom", "There are blankets on the bed.", None, 'master', None, 'living', None, None)
living = Room("Living Room", "You are at the center of the house.", None, 'bathroom', 'bedroom', 'kitchen', None, None)
bathroom = Room("Bathroom", "You are in the bathroom.", 'living', None, 'master', 'patio', None, None)
kitchen = Room("Kitchen", "You are in the kitchen.", None, 'patio', 'living', None, None, None)
patio = Room("Patio", "You are on the patio. You can leave the house to the south.", 'kitchen', 'gas', 'bathroom', None, None, None)
gas = Room("Gas", "You are in the kitchen.", None, 'tower', 'master', None, None, None)
tower = Room("Tower", "You are inside the tower. The tower has 3 levels.",'gas', 'storage', 'playground', None, 'second', None)
second = Room("Second Level", "You are on the second level of the tower.", None, None, None, None, 'third', 'tower')
third = Room("Third Level", "You are on the third level of the tower.", None, None, None, None, None, 'second')
storage = Room("Storage Container", "You are inside the storage container.", 'tower',None, None, None, None, None)
shed = Room("Shed", "You are inside the shed.", 'playground', 'car', None, None, None, None)
car = Room("Car", "The car is outside.", 'shed', None, None, None, None, None)
lake = Room("Lake", "The lake is looking nice today.", None, None, None, 'playground', None, None)

current_node = playground
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
directions = ['north', 'south', 'east', 'west', 'up', 'down']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        #look for which command we typed in
        pos = short_directions.index(command)
        # change the command to be the long form
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You can't go that way.")
    else:
        print("Command not recognized.")

