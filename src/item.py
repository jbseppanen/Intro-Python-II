# Class to hold item information


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"The {self.name.lower()} has been picked up.")

    def on_drop(self):
        print(f"The {self.name.lower()} has been dropped.")
