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
        if not self.items:
            print("This room contains no items.")
        else:
            print("This room has the following items: ")
            for i in self.items:
                print(i.name)

    def print_valid_directions(self):
        valid_directions = []
        if self.n_to is not None:
            valid_directions.append("North(n)")
        if self.e_to is not None:
            valid_directions.append("East(e)")
        if self.s_to is not None:
            valid_directions.append("South(s)")
        if self.w_to is not None:
            valid_directions.append("West(w)")

        print_string = "You can go "

        for i in range(0, len(valid_directions)):
            print_string += valid_directions[i]
            if i + 2 < len(valid_directions):
                print_string += ", "
            elif i + 1 < len(valid_directions):
                print_string += " or "
            else:
                print_string += "."

        print(print_string)

    def enter_room(self):
        print(f"You are in the {self.name}.")
        print(self.description)
        self.print_valid_directions()
        self.print_items()
