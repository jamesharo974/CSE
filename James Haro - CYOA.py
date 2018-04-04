class Items(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def name(self):
        print("The name of the item is %s" % self.name)

    def description(self):
        print("This item's description is %s" % self.description)


class Healing(Items):
    def __init__(self, name, description, add_health, consumable):
        super(Healing, self).__init__(name, description)
        self.add_health = add_health
        self.consumable = consumable

        def add_health(self):
            print("You have now gained health by %s" % name)

        def consumable(self):
            print("Your item is a %s" % self.consumable)


class Apple(Healing):
    def __init__(self, name, description, add_health, consumable):
        super(Apple, self).__init__(name, description, add_health, consumable)


class Medicine(Healing):
    def __init__(self, name, description, add_health, consumable):
        super(Medicine, self).__init__(name, description, add_health, consumable)


class Antibiotic(Healing):
    def __init__(self, name, description, add_health, consumable):
        super(Antibiotic, self).__init__(name, description, add_health, consumable)


class Weapon(Items):
    def __init__(self, name, description, attack):
        super(Weapon, self).__init__(name, description)
        self.attack = attack

        def pick_up(self):
            print("You picked up a %s" % name)

        def attack(self):
            print("you attacked with a %s" % name)


class Sword(Weapon):
    def __init__(self, name, description, attack):
        super(Sword, self).__init__(name, description, attack)


class Pocket_Knife(Weapon):
    def __init__(self, name, description, attack):
        super(Pocket_Knife, self).__init__(name, description, attack)


class Tools(Items):
    def __init__(self, name, description, use):
        super(Tools, self).__init__(name, description)
        self.use = use

        def pick_up(self):
            print("You picked up a %s" % name)

        def attack(self):
            print("you attacked with a %s" % name)


class Pencil(Tools):
    def __init__(self, name, description, attack):
        super(Pencil, self).__init__(name, description, attack)


class Crow_bar(Tools):
    def __init__(self, name, description, attack):
        super(Crow_bar, self).__init__(name, description, attack)


class Clothing(Items):
    def __init__(self, name, description, put_on):
        super(Clothing, self).__init__(name, description)
        self.put_on = put_on

        def put_on(self):
            print("You put on a %s" % name)


class Pants(Clothing):
    def __init__(self, name, description, put_on):
        super(Pants, self).__init__(name, description, put_on)


class Hat(Clothing):
    def __init__(self, name, description, put_on):
        super(Hat, self).__init__(name, description, put_on)


class Vest(Clothing):
    def __init__(self, name, description, put_on):
        super(Vest, self).__init__(name, description, put_on)


class Hoodie(Clothing):
    def __init__(self, name, description, put_on):
        super(Hoodie, self).__init__(name, description, put_on)


class Character(object):
    def __init__(self, health, abilities, description, inventory, name):
        self.health = 100
        self.abilities = abilities
        self.description = description
        self.inventory = inventory
        self.name = name


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

player1 = Character("100", "run", "tall, slim and smart", "sword", "Pegasus")

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
