# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

    def pickup_item(self, item):
        if self.room.items.count(item) > 0:
            self.items.append(item)
            self.room.items.remove(item)
            item.on_take()
        else:
            print(f"A {item.name} is not in this room.")

    def drop_item(self, item):
        if self.items.count(item) > 0:
            self.room.items.append(item)
            self.items.remove(item)
            item.on_drop()
        else:
            print(f"You do not have a {item.name} to drop.")

    def print_items(self):
        if not self.items:
            print("You have no items.")
        else:
            print("You have the following items: ")
            for i in self.items:
                print(i.name)

