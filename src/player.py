# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def pickup(self, item):
        self.items.append(item)


class Item:
    def __init__(self, name):
        self.name = name
