# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def print_items(self):
        print("This room has the following items: ")
        for i in self.items:
            print(i.name)

    def enter_room(self):
        print(f"You are in the {self.name}.")
        print(self.description)

