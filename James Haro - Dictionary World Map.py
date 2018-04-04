world_map = {
    'PLAYGROUND': {
        'NAME' : "Playground",
        'DESCRIPTION': "You are at the playground.",
        'PATHS': {
            'NORTH': 'GARAGE',
            'SOUTH': 'SHED',
            'EAST': 'LAKE',
            'WEST': 'TOWER'
        }
    },
    'GARAGE' : {
        'NAME' : 'Garage',
        'DESCRIPTION' : "The car is not here.",
        'PATHS' : {
            'SOUTH' : 'PLAYGROUND',
            'NORTH' : 'MASTER'
        }
    },
    'MASTER' : {
       'NAME' : 'Master Bedroom',
        'DESCRIPTION' : "You just entered the house. Wow what a big room.",
        'PATHS' : {
            'NORTH' : 'BEDROOM',
            'WEST' : 'BATHROOM',
            'SOUTH' : 'GARAGE'
        }
    },
    'ROOM': {
        'NAME': 'Bedroom',
        'DESCRIPTION': "There are blankets on the bed.",
        'PATHS': {
            'WEST': 'LIVING',
            'SOUTH': 'MASTER'
        }
    },
    'LIVING': {
        'NAME': 'Living Room',
        'DESCRIPTION': "You are in the center of the ",
        'PATHS': {
            'WEST': 'KITCHEN',
            'SOUTH': 'BATHROOM',
            'EAST': 'ROOM'
        }
    },
    'BATH': {
        'NAME': 'Bathroom',
        'DESCRIPTION': "You are in the bathroom.",
        'PATHS': {
            'WEST': 'PATIO',
            'NORTH': 'LIVING',
            'EAST': 'MASTER',
        }
    },
    'KITCHEN': {
        'NAME': 'Kitchen',
        'DESCRIPTION': "You are in the kitchen.",
        'PATHS': {
            'SOUTH': 'PATIO',
            'EAST': 'MASTER',
        }
    },
    'PATIO': {
        'NAME': 'Patio',
        'DESCRIPTION': "You are on the patio. You can leave the house to the south.",
        'PATHS': {
            'SOUTH': 'GAS',
            'NORTH': 'KITCHEN',
            'EAST': 'BATH',
        }
    },
    'GAS': {
        'NAME': 'Gas Tank',
        'DESCRIPTION': "You are right outside the house. You can enter the house to the south.",
        'PATHS': {
            'SOUTH': 'TOWER',
            'NORTH': 'PATIO',
        }
    },
    'TOWER': {
        'NAME': 'Tower',
        'DESCRIPTION': "You are inside the tower. The tower has 3 levels.",
        'PATHS': {
            'SOUTH': 'STORAGE',
            'NORTH': 'GAS',
            'EAST': 'PLAYGROUND',
            'UP': 'SECOND',
        }
    },
    'SECOND': {
        'NAME': 'Second Level',
        'DESCRIPTION': "You are on the second level of the tower.",
        'PATHS': {
            'UP': 'THIRD',
            'DOWN': 'TOWER',
        }
    },
    'THIRD': {
        'NAME': 'Third Level',
        'DESCRIPTION': "You are on the third level of the tower.",
        'PATHS': {
            'DOWN': 'SECOND',
        }
    },
    'STORAGE': {
        'NAME': 'Storage Container',
        'DESCRIPTION': "You are inside the storage container.",
        'PATHS': {
            'NORTH': 'TOWER',
        }
    },
    'SHED': {
        'NAME': 'Shed',
        'DESCRIPTION': "You are inside the shed.",
        'PATHS': {
            'NORTH': 'PLAYGROUND',
            'SOUTH': 'CAR',
        }
    },
    'CAR': {
        'NAME': 'Car',
        'DESCRIPTION': "The car is outside.",
        'PATHS': {
            'NORTH': 'SHED',
        }
    },
    'LAKE': {
        'NAME': 'lake',
        'DESCRIPTION': "The lake is looking nice today.",
        'PATHS': {
            'WEST': 'PLAYGROUND',
        }
    },
}

current_node = world_map['PLAYGROUND']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way")
    else:
        print('Command not Recognized')