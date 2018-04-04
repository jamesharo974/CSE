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
            