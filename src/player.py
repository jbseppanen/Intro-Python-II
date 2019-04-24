# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []

    def pickup(self, item):
        if self.room.items.count(item) > 0:
            self.inventory.append(item)
            self.room.items.remove(item)
            print(f"The {item.name} has been picked up.")
        else:
            print(f"A {item.name} is not in this room.")
