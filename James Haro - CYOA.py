import sys

def Fight(target):
    while player1.health > 0 and target.health > 0:
        print("You have %d Health left" % player1.health)
        print("Target has %d Health left" % target.health)
        cmd = input("What do you want to do?")
        if cmd == 'attack':
            player1.attack(target)
        if target.health > 0:
            target.attack(player1)
        if target.health <= 0:
            print("You killed the Goblin.")
        if player1.health <= 0:
            print("You Died")
            sys.exit(0)

class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def name(self):
        print("The name of the item is %s" % self.name)

    def description(self):
        print("This item's description is %s" % self.description)


class Healing(Item):
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


class Weapon(Item):
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


class Tools(Item):
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


class CrowBar(Tools):
    def __init__(self, name, description, attack):
        super(CrowBar, self).__init__(name, description, attack)
        self.attack = attack


class Clothing(Item):
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
    def __init__(self, health, abilities, description, inventory, name, weapon):
        self.health = health
        self.abilities = abilities
        self.description = description
        self.inventory = inventory
        self.name = name
        self.weapon = weapon

    def attack(self, enemy):
        enemy.take_damage(self.weapon.attack)

    def take(self, item):
        self.inventory.append(item)
        print("You picked up the %s" % item.name)

    def take_damage(self, amt):
        self.health -= amt


class Room(object):
    def __init__(self, name, description, north, south, east, west, up, down, item=None, enemy=None):
        if item is None:
            items = []
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.items = item
        self.enemy = enemy

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


crowbar1 = CrowBar("Crowbar", "It can open a door", 35)


class Goblin(Character):
    def __init__(self):
        super(Goblin, self).__init__(100, "fight", "big and ugly", [], "James", crowbar1)




healing = Healing("Healing", "These items can heal you.", 20, "This item is consumable.")

apple = Apple("Apple", "This apple can give you health.", 15, "This item is consumable.")

medicine = Medicine("Medicine", "This medicine restores some of your health", 40, "This item is consumable.")

antibiotic = Antibiotic("Antibiotic", "This type of medicine restores the most health", 60, "This item is consumable.")

weapon = Weapon("Weapons", "These items cause damage.", 35)

sword = Sword("Sword", "This weapon causes 35 attack damage when swung.", 55)

pocket_knife = Pocket_Knife("Pocket Knife", "This specific weapon can cause 35 damage.", 35)

tools = Tools("Tools", "These tools can be used.", "You can use it.")

pencil = Pencil("Pencil", "This pencil can write on things and can be a weapon.", 35)

clothing = Clothing("Clothes", "These items give health protection.", "These can be worn")

pants = Pants("Pants", "These pants protect you from the cold.", "These are wearable.")

hat = Hat("Hat", "The hat helps protect from the sun", "The hat is wearable")

vest = Vest("Vest", "This vest protects from weapons", "This vest is wearable.")

hoodie = Hoodie("Hoodie", "This hoodie provides protect from the cold.", "This hoodie is wearable.")

player1 = Character(100, "hide", "short and helpfull", [], "Jonathan Johnson", sword)
print(player1.name)
print("Health: %s" % player1.health)
print("Inventory: %s" % player1.inventory)

playground = Room("Playground", "You are at the playground. There is also a crowbar here.", 'garage', 'shed', 'lake',
                  'tower', None, None, [crowbar1])

garage = Room("Garage", "The car is not here. There are also tools here.", 'master', 'playground', None, None, None,
              None, [tools], Goblin())

master = Room("Master Bedroom", "You just entered the house. Wow what a big room. There is also a clothing here.",
              'bedroom', 'garage', None, 'bathroom', None, None, [clothing])

bedroom = Room("Bedroom", "There are blankets on the bed. There is also a pencil and hat here.", None, 'master', None,
               'living', None, None, [pencil, hat])

living = Room("Living Room", "You are at the center of the house. There is also a weapon here.", None, 'bathroom',
              'bedroom', 'kitchen', None, None, [weapon])

bathroom = Room("Bathroom", "You are in the bathroom. There is medicine, healing and antibiotic here. ", 'living', None,
                'master', 'patio', None, None, [medicine, healing, antibiotic])

kitchen = Room("Kitchen", "You are in the kitchen. There is also an apple here.", None, 'patio', 'living', None, None,
               None, [apple])

patio = Room("Patio", "You are on the patio. You can leave the house to the south. There is also an apple here.",
             'kitchen', 'gas', 'bathroom', None, None, None, [apple])

gas = Room("Gas", "You are in the kitchen. There is also a sword here.", None, 'tower', 'master', None, None, None,
           [sword])

tower = Room("Tower", "You are inside the tower. The tower has 3 levels. There is a vest and a hoodie here.", 'gas',
             'storage', 'playground', None, 'second', None, [vest, hoodie])

second = Room("Second Level", "You are on the second level of the tower. There are some pants here.", None, None, None,
              None, 'third', 'tower', [pants], Goblin())

third = Room("Third Level", "You are on the third level of the tower. There is also a pocket knife here.", None, None,
             None, None, None, 'second', [pocket_knife])

storage = Room("Storage Container", "You are inside the storage container. There are some pants and a sword here.",
               'tower', None, None, None, None, None, [pants, sword])

shed = Room("Shed", "You are inside the shed. There is also medicine here.", 'playground', 'car', None, None, None,
            None, [medicine], Goblin())

car = Room("Car", "The car is outside. There are also tools here.", 'shed', None, None, None, None, None, [tools])

lake = Room("Lake", "The lake is looking nice today. There is also an apple here.", None, None, 'boat', 'playground',
            None, None, [apple])

boat = Room("Boat", "The boat is right on the lake.", None, None, None, 'lake', None, None)


current_node = playground

short_directions = ['n', 's', 'e', 'w', 'u', 'd']

directions = ['north', 'south', 'east', 'west', 'up', 'down']


while True:
    print(current_node.name)
    print(current_node.description)

    if current_node.enemy is not None:
        print("You see %s" % current_node.enemy.name)
        Fight(current_node.enemy)
        if player1.health <= 0:
            sys.exit(0)
        current_node.enemy = None
        continue
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # look for which command we typed in
        pos = short_directions.index(command)
        # change the command to be the long form
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You can't go that way.")
    elif "take" in command:
        item_requested = command[5:]
        for item in current_node.items:
            if item.name.lower() == item_requested.lower():
                player1.take(item)
    elif "use" in command:
        item_requested = command[5:]
        for item in player1.inventory:
            if item.name.lower() == item_requested.lower():
                player1.take(item)
                print("You used %s" % player1.inventory)

    else:
        print("Command not recognized.")



