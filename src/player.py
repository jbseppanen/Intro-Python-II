# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []

    def pickup_item(self, item):
        if self.room.items.count(item) > 0:
            self.inventory.append(item)
            self.room.items.remove(item)
            print(f"The {item.name} has been picked up.")
        else:
            print(f"A {item.name} is not in this room.")

    def drop_item(self, item):
        if self.inventory.count(item) > 0:
            self.room.items.append(item)
            self.inventory.remove(item)
            print(f"The {item.name} has been dropped.")
        else:
            print(f"You do not have a {item.name} to drop.")
