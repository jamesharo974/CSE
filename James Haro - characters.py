class Character(object):
    def __init__(self, health, abilities, description, inventory, name):
        self.health = 100
        self.abilities = abilities
        self.description = description
        self.inventory = inventory
        self.name = name

player = Character("100", "run", "tall, slim and smart", "sword", "Pegasus")