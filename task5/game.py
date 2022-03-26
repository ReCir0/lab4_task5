'''Lab 4.5'''

enemy_counter = 0

class Room():
    '''
    class that represents a room
    '''
    def __init__(self, name):
        '''
        init function
        '''
        self.name = name
        self.description = None
        self.linked_rooms = []
        self.character = None
        self.item = None

    def set_description(self, description):
        '''
        Sets a description for a room object
        '''
        self.description = description

    def link_room(self, room, direction):
        '''
        Links a room
        '''
        self.linked_rooms.append((room, direction))

    def set_character(self, character):
        '''
        Sets a character to a specific room
        '''
        self.character = character

    def set_item(self, item):
        '''
        Sets a character to a specific room
        '''
        self.item = item

    def get_details(self):
        '''
        Gets details of a room
        '''
        print(self.name)
        print('--------------------')
        print(self.description)
        for room in self.linked_rooms:
            print("The " + room[0].name + ' is ' + room[1])

    def get_character(self):
        '''
        Gets character of a room
        '''
        return self.character

    def get_item(self):
        '''
        Gets item of a room
        '''
        return self.item

    def move(self, direction):
        '''
        Function that makes a move
        '''
        for item in self.linked_rooms:
            if item[1] == direction:
                return item[0]

class Enemy():
    '''
    Class that represents an enemy
    '''
    def __init__(self, name, description):
        '''
        Init function
        '''
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None
        self.monsters = 0

    def set_conversation(self, text):
        '''
        Sets a conversation
        '''
        self.conversation = text

    def set_weakness(self, weakness):
        '''
        Sets a weakness for an enemy
        '''
        self.weakness = weakness

    def describe(self):
        '''
        Describes an enemy
        '''
        print(f'{self.name} is here!')
        print(self.description)

    def talk(self):
        '''
        Makes an enemy talk
        '''
        print(f'[{self.name} says]: {self.conversation}')

    def fight(self, item_to_fight):
        '''
        Function that helps to fight
        '''
        if self.weakness == item_to_fight:
            print(f"You fend {self.name} off with the {item_to_fight}")
            global enemy_counter
            enemy_counter += 1
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False

    @staticmethod
    def get_defeated():
        '''
        Checks if you finished the game
        '''
        return enemy_counter

class Item():
    '''
    Class that represents an item
    '''
    def __init__(self, name):
        '''
        Init method
        '''
        self.name = name
        self.description = None

    def set_description(self, text):
        '''
        Sets a description
        '''
        self.description = text

    def describe(self):
        '''
        Describes an item
        '''
        print(f'The [{self.name}] is here - {self.description}')

    def get_name(self):
        '''
        Gets item name
        '''
        return self.name
