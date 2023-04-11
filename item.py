class Item:
    items = list()

    def __init__(self, location: int, is_visible: bool, name: str, location_text: str, description: str):
        self.location = location
        self.is_visible = is_visible
        self.name = name
        self.location_text = location_text
        self.description = description
        self.discovered = False
        self.items.append(self)

    def inspect(self):
        return print(self.description)


class Reveal(Item):
    def __init__(self, location, is_visible, reveals, condition, name, location_text, description, empty):
        super().__init__(location, is_visible, name, location_text, description)
        self.reveals = reveals
        self.condition = condition
        self.empty = empty


class Movable(Item):

    def __init__(self, location: int, is_visible: bool, name: str, location_text: str, description: str, dropped: str):
        super().__init__(location, is_visible, name, location_text, description)
        self.dropped = dropped
        self.moved = False


class Consumable(Movable):
    def __init__(self, location: int, is_visible: bool, food: int, drink: int, name, location_text: str,
                 description: str, dropped: str, consumed: str):
        super().__init__(location, is_visible, name, location_text, description, dropped)
        self.food = food
        self.drink = drink
        self.consumed = consumed

    def inspect(self):
        return print(f"{self.description}\nFood: {self.food}. Drink: {self.drink}.")


class Dashboard(Item):
    def __init__(self, location: int, is_visible: bool, reveals: type(Item), name: str, location_text: str,
                 description: str, key_false: str, key_true: str, power_false: str, power_true: str, fuel_false: str,
                 fuel_true: str):
        super().__init__(location, is_visible, name, location_text, description)
        self.reveals = reveals
        self.key_false = key_false
        self.key_true = key_true
        self.power_false = power_false
        self.power_true = power_true
        self.fuel_false = fuel_false
        self.fuel_true = fuel_true
        self.key = False
        self.power = False
        self.fuel = False

    def inspect(self):
        # No items
        if not self.key and not self.power and not self.fuel:
            return print(f"{self.key_false}\n{self.power_false}\n{self.fuel_false}\n{self.description}")
        # Only key
        elif self.key and not self.power and not self.fuel:
            return print(f"{self.key_true}\n{self.power_false}\n{self.fuel_false}\n{self.description}")
        # Only power
        elif not self.key and self.power and not self.fuel:
            return print(f"{self.key_false}\n{self.power_true}\n{self.fuel_false}\n{self.description}")
        # Only fuel
        elif not self.key and not self.power and self.fuel:
            return print(f"{self.key_false}\n{self.power_false}\n{self.fuel_true}\n{self.description}")
        # Key and power
        elif self.key and self.power and not self.fuel:
            return print(f"{self.key_true}\n{self.power_true}\n{self.fuel_false}\n{self.description}")
        # Key and fuel
        elif self.key and not self.power and self.fuel:
            return print(f"{self.key_true}\n{self.power_false}\n{self.fuel_true}\n{self.description}")
        # Power and fuel
        elif not self.key and self.power and self.fuel:
            return print(f"{self.key_false}\n{self.power_true}\n{self.fuel_true}\n{self.description}")
        # Key, Power and Fuel
        elif self.key and self.power and self.fuel:
            return print(f"{self.key_true}\n{self.power_true}\n{self.fuel_true}\n{self.description}")
        else:
            return print("Write more code for this")


class Compartment(Item):
    def __init__(self, location: int, is_visible: bool, insertable: list[Item], name: str, location_text: str,
                 description: str, description_opened, battery_false, battery_true, power_cable_false, power_cable_true):
        super().__init__(location, is_visible, name, location_text, description)
        self.insertable = insertable
        self.description_opened = description_opened
        self.battery_false = battery_false
        self.battery_true = battery_true
        self.power_cable_false = power_cable_false
        self.power_cable_true = power_cable_true
        self.open = False
        self.battery = False
        self.cable = False

    def Inspect(self):
        if not self.open:
            return print(self.description)
        else:
            if not self.battery and not self.cable:
                return print(f"{self.description_opened}\n{self.battery_false}\n{self.power_cable_false}")
            elif not self.battery and self.cable:
                return print(f"{self.description_opened}\n{self.battery_false}\n{self.power_cable_true}")
            elif self.battery and not self.cable:
                return print(f"{self.description_opened}\n{self.battery_true}\n{self.power_cable_false}")
            elif self.battery and self.cable:
                return print(f"{self.description_opened}\n{self.battery_true}\n{self.power_cable_true}")
            else:
                return print("Add more code for this")


class HeavyChest(Item):
    def __init__(self, location, is_visible, reveals, holds, name, location_text, description, full, empty):
        super().__init__(location, is_visible, name, location_text, description)
        self.reveals = reveals
        self.holds = holds
        self.full = full
        self.empty = empty
        self.locked = True


class Requires(Item):
    def __init__(self, location, is_visible, insertable, name, location_text, description, empty, full):
        super().__init__(location, is_visible, name, location_text, description)
        self.insertable = insertable
        self.inserted = None
        self.empty = empty
        self.full = full


class Holds(Item):
    def __init__(self, location, is_visible, reveals, holds, name, location_text, description, empty):
        super().__init__(location, is_visible, name, location_text, description)
        self.reveals = reveals
        self.holds = holds
        self.empty = empty


class Container(Holds):
    def __init__(self, location, is_visible, reveals, holds, name, location_text, description, full, empty):
        super().__init__(location, is_visible, reveals, holds, name, location_text, description, empty)
        self.full = full
        self.open = False



    def Inspect(self):
        if not self.open:
            return print(self.description)
        elif self.open and self.item is not None:
            return print(self.description)
        elif self.open and self.item is None:
            return print(self.when_empty)
        else:
            return print("Error Notice")

    def Open(self):
        if self.locked:
            return print(f"{self.name} is locked.")
        elif self.open:
            return print(f"{self.name} is already open.")
        else:
            self.open = True
            return print(f"{self.name} opened.")


class HasItem(Item):
    def __init__(self, location, is_visible, child, item, name, location_text, description, when_empty):
        super().__init__(location, is_visible, name, location_text, description)
        self.child = child
        self.when_empty = when_empty
        self.item = item

    def Inspect(self):
        if self.item is not None:
            return print(self.description)
        else:
            return print(self.when_empty)


class ConditionalHasItem(HasItem):
    def __init__(self, location, is_visible, child, item, name, location_text, description, when_empty):
        super().__init__(location, is_visible, child, item, name, location_text, description, when_empty)
        self.condition_met = False


class ContainerHasItem(HasItem):
    def __init__(self, location, is_visible, child, item, name, location_text, description, when_full, when_empty):
        super().__init__(location, is_visible, child, item, name, location_text, description, when_empty)
        self.when_full = when_full
        self.open = False

    def Inspect(self):
        if not self.open:
            return print(self.description)
        else:
            if self.item is not None:
                return print(self.when_full)
            else:
                return print(self.when_empty)

    def Open(self):
        if self.open:
            return print(f"{self.name} is already open.")
        else:
            self.open = True
            return print(f"{self.name} opened.")

    def Close(self):
        if not self.open:
            print(f"{self.name} is already closed.")
        else:
            self.open = False
            return print(f"{self.name} closed.")


class ContainerNeedItem(ContainerHasItem):
    def __init__(self, location, is_visible, child, item, item_needed, name, location_text, description, when_full,
                 when_empty):
        super().__init__(location, is_visible, child, item, name, location_text, description, when_full, when_empty)
        self.when_full = when_full
        self.when_empty = when_empty
        self.open = False
        self.item = item
        self.item_needed = item_needed








'''
class MobileContainerItem(MobileItem):
    def __init__(self, name, starting_location, is_visible, description,
                 location_text, dropped_location_text):
        super().__init__(name, starting_location, is_visible, description,
                         location_text, dropped_location_text)
        self.items = list()
'''
