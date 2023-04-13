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


class Movable(Item):
    movable_items = list()

    def __init__(self, location: int, is_visible: bool, name: str, location_text: str, description: str):
        super().__init__(location, is_visible, name, location_text, description)
        self.moved = False
        self.movable_items.append(self)


class Conditional(Item):
    def __init__(self, location: int, is_visible: bool, name: str, location_text: str, description: str):
        super().__init__(location, is_visible, name, location_text, description)
        self.condition_met = False


class Consumable(Movable):
    def __init__(self, location: int, is_visible: bool, food: int, drink: int, name, location_text: str,
                 description: str, consumed: str):
        super().__init__(location, is_visible, name, location_text, description)
        self.food = food
        self.drink = drink
        self.consumed = consumed

    def inspect(self):
        return print(f"{self.description}\nFood: {self.food}. Drink: {self.drink}.")


class WaterBottle(Consumable):
    def __init__(self, location: int, is_visible: bool, food: int, drink: int, name, location_text: str,
                 description: str, consumed: str, empty: str):
        super().__init__(location, is_visible, food, drink, name, location_text, description, consumed)
        self.is_full = True
        self.empty = empty


class Reveals(Item):
    def __init__(self, location: int, is_visible: bool, reveals: type(Item), name: str, location_text: str,
                 description: str):
        super().__init__(location, is_visible, name, location_text, description)
        self.reveals = reveals


class RevealsMovable(Reveals):
    def __init__(self, location: int, is_visible: bool, reveals: type(Item), name: str, location_text: str,
                 description: str, empty: str):
        super().__init__(location, is_visible, reveals, name, location_text, description)
        self.taken = False
        self.empty = empty

    def inspect(self):
        if not self.taken:
            print(self.description)
        else:
            print(self.empty)


class Revealed(Item):
    def __init__(self, location: int, is_visible: bool, revealed_by: type(Item), name: str, location_text: str,
                 description: str):
        super().__init__(location, is_visible, name, location_text, description)
        self.revealed_by = revealed_by


class RevealedMovable(Revealed, Movable):
    def __init__(self, location: int, is_visible: bool, revealed_by: type(Item), name: str, location_text: str,
                 description: str):
        super().__init__(location, is_visible, revealed_by, name, location_text, description)


class ConditionalReveals(Reveals, Conditional):
    def __init__(self, location: int, is_visible: bool, reveals: type(Item), name: str, location_text: str,
                 description: str, reveal_text: str):
        super().__init__(location, is_visible, reveals, name, location_text, description)
        self.reveal_text = reveal_text

    def inspect(self):
        if not self.condition_met:
            print(self.description)
        elif self.condition_met:
            print(self.reveal_text)
        else:
            print("An error occurred.")


class ConditionalRevealsMovable(RevealsMovable):
    def __init__(self, location: int, is_visible: bool, reveals, name, location_text, description, empty):
        super().__init__(location, is_visible, reveals, name, location_text, description, empty)


class RequiresInsert(Item):
    def __init__(self, location, is_visible, name, location_text, description, full):
        super().__init__(location, is_visible, name, location_text, description)
        self.insert = False
        self.full = full

    def inspect(self):
        if not self.insert:
            return print(self.description)
        else:
            return print(self.full)


class FinalButton(Item):
    def __init__(self, location, is_visible, name, location_text, description, inactive, active):
        super().__init__(location, is_visible, name, location_text, description)
        self.condition = False
        self.inactive = inactive
        self.active = active

    def pressed(self):
        if not self.condition:
            return print(self.inactive)
        elif self.condition:
            return print(self.active)
        else:
            return print("Final Button Error")


class Dashboard(Reveals):
    def __init__(self, location: int, is_visible: bool, reveals: type(Item), name: str, location_text: str,
                 description: str, key_false: str, key_true: str, power_false: str, power_true: str, fuel_false: str,
                 fuel_true: str):
        super().__init__(location, is_visible, reveals, name, location_text, description)
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
    def __init__(self, location: int, is_visible: bool, name: str, location_text: str,
                 description: str, battery_false: str, battery_true: str, power_cable_false: str,
                 power_cable_true: str):
        super().__init__(location, is_visible, name, location_text, description)
        self.battery_false = battery_false
        self.battery_true = battery_true
        self.power_cable_false = power_cable_false
        self.power_cable_true = power_cable_true
        self.battery = False
        self.cable = False

    def inspect(self):
        if not self.battery and not self.cable:
            return print(f"{self.description}\n{self.battery_false}\n{self.power_cable_false}")
        elif not self.battery and self.cable:
            return print(f"{self.description}\n{self.battery_false}\n{self.power_cable_true}")
        elif self.battery and not self.cable:
            return print(f"{self.description}\n{self.battery_true}\n{self.power_cable_false}")
        elif self.battery and self.cable:
            return print(f"{self.description}\n{self.battery_true}\n{self.power_cable_true}")
        else:
            return print("Error in compartment")


class HeavyChest(Item):
    def __init__(self, location, is_visible, reveals, holds, name, location_text, description, full, empty):
        super().__init__(location, is_visible, name, location_text, description)
        self.reveals = reveals
        self.holds = holds
        self.full = full
        self.empty = empty
        self.locked = True


class Water(Consumable):
    def __init__(self, location: int, is_visible: bool, food: int, drink: int, name, location_text: str,
                 description: str, consumed: str):
        super().__init__(location, is_visible, food, drink, name, location_text, description, consumed)


class Buoy(Reveals):
    def __init__(self, location: int, is_visible: bool, reveals: type(Item), name: str, location_text: str,
                 description: str, jerry_true: str, jerry_false: str, cable_true: str, cable_false: str):
        super().__init__(location, is_visible, reveals, name, location_text, description)
        self.jerry = True
        self.Cable = True
        self.jerry_true = jerry_true
        self.jerry_false = jerry_false
        self.cable_true = cable_true
        self.cable_false = cable_false
