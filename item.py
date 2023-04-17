# A base item that all inherit off.
class Base:
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
        return self.description


# Container items.
class Container(Base):
    containers = list()

    def __init__(self, location: int, is_visible: bool, locked: bool, name: str, location_text: str, description: str):
        super().__init__(location, is_visible, name, location_text, description)
        self.locked = locked
        self.open = False
        self.containers.append(self)


# If an item requires a condition to be met before it can complete something.
class Conditional(Base):
    def __init__(self, location: int, is_visible: bool, name: str, location_text: str, description: str):
        super().__init__(location, is_visible, name, location_text, description)
        self.condition_met = False


# Movable items.
# Basic.
class Movable(Base):
    movable_items = list()

    def __init__(self, location: int, is_visible: bool, name: str, location_text: str, description: str):
        super().__init__(location, is_visible, name, location_text, description)
        self.moved = False
        self.movable_items.append(self)


# A movable item that has been revealed by another.
class RevealedMovable(Movable):
    def __init__(self, location: int, is_visible: bool, revealed_by: type(Base), name: str, location_text: str,
                 description: str):
        super().__init__(location, is_visible, name, location_text, description)
        self.revealed_by = revealed_by


class ConditionalRevealedMovable(RevealedMovable, Conditional):
    def __init__(self, location: int, is_visible: bool, revealed_by: type(Base), name: str, location_text: str,
                 description: str):
        super().__init__(location, is_visible, revealed_by, name, location_text, description)


# Food items that can be consumed.
class Consumable(Movable):
    def __init__(self, location: int, is_visible: bool, food: int, drink: int, name, location_text: str,
                 description: str, consumed: str):
        super().__init__(location, is_visible, name, location_text, description)
        self.food = food
        self.drink = drink
        self.consumed = consumed

    def inspect(self):
        return f"{self.description}\nFood: {self.food}   Drink: {self.drink}."


# A movable item that has been revealed by another.
class RevealedConsumable(Consumable):
    def __init__(self, location: int, is_visible: bool, food: int, drink: int, revealed_by: type(Base), name: str,
                 location_text: str, description: str, consumed):
        super().__init__(location, is_visible, food, drink, name, location_text, description, consumed)
        self.revealed_by = revealed_by


# An item that when inspected, reveals another.
# Basic.
class Reveals(Base):
    def __init__(self, location: int, is_visible: bool, reveals: type(Base), name: str, location_text: str,
                 description: str):
        super().__init__(location, is_visible, name, location_text, description)
        self.reveals = reveals

    def inspect(self):
        self.reveals.is_visible = True
        return self.description


# If there is a condition before the item reveals another.
class ConditionalReveals(Reveals, Conditional):
    def __init__(self, location: int, is_visible: bool, reveals: type(Base), name: str, location_text: str,
                 description: str, reveal_text: str):
        super().__init__(location, is_visible, reveals, name, location_text, description)
        self.reveal_text = reveal_text

    def inspect(self):
        self.reveals.is_visible = True
        if not self.condition_met:
            return self.description
        elif self.condition_met:
            return self.reveal_text
        else:
            print("An error occurred.")


# If the item reveals a movable item.
class RevealsMovable(Reveals):
    def __init__(self, location: int, is_visible: bool, reveals: type(Base), name: str, location_text: str,
                 description: str, item_one_true: str, item_one_false: str):
        super().__init__(location, is_visible, reveals, name, location_text, description)
        self.item_one_taken = False
        self.item_one_true = item_one_true
        self.item_one_false = item_one_false

    def inspect(self):
        self.reveals.is_visible = True
        if not self.item_one_taken:
            return f"{self.description}\n{self.item_one_true}"
        else:
            return self.item_one_false


# If a condition must be met before a movable item is revealed.
class ConditionalRevealsMovable(RevealsMovable, Conditional):
    def __init__(self, location: int, is_visible: bool, reveals: type(Base), name: str, location_text: str,
                 description: str, item_one_true: str, item_one_false: str):
        super().__init__(location, is_visible, reveals, name, location_text, description, item_one_true, item_one_false)

    def inspect(self):
        if not self.condition_met:
            return f"{self.description}\n{self.item_one_false}"
        elif self.condition_met and not self.item_one_taken:
            self.reveals.is_visible = True
            return f"{self.description}\n{self.item_one_true}"
        elif self.condition_met and self.item_one_taken:
            return f"{self.description}\n{self.item_one_false}"
        else:
            return "***ERROR MESSAGE***"


# If the item reveals two movable items.
class DualRevealsMovable(RevealsMovable):
    def __init__(self, location: int, is_visible: bool, reveals: list[type(Base)], name: str, location_text: str,
                 description: str, item_one_true: str, item_one_false: str, item_two_true: str, item_two_false: str):
        super().__init__(location, is_visible, reveals, name, location_text, description, item_one_true, item_one_false)
        self.item_two_taken = False
        self.item_two_true = item_two_true
        self.item_two_false = item_two_false

    def inspect(self):
        for item in self.reveals:
            item.is_visible = True
        if not self.item_one_taken and not self.item_two_taken:
            return f"{self.description}\n{self.item_one_true}\n{self.item_two_true}"
        elif not self.item_one_taken and self.item_two_taken:
            return f"{self.description}\n{self.item_one_true}\n{self.item_two_false}"
        elif self.item_one_taken and not self.item_two_taken:
            return f"{self.description}\n{self.item_one_false}\n{self.item_two_true}"
        elif self.item_one_taken and self.item_two_taken:
            return f"{self.description}\n{self.item_one_false}\n{self.item_two_false}"
        else:
            return "An error has occurred. Please report the error code to the game design team."


# If the item requires something to be inserted.
class RequiresInsert(Base):
    def __init__(self, location, is_visible, name, location_text, description, full):
        super().__init__(location, is_visible, name, location_text, description)
        self.insert = False
        self.full = full

    def inspect(self):
        if not self.insert:
            return self.description
        else:
            return self.full


# Non Player Characters.
class Npc(Base):
    def __init__(self, location: int, is_visible: bool, name: str, location_text: str, description: str,
                 initial_text: str):
        super().__init__(location, is_visible, name, location_text, description)
        self.initial_text = initial_text


# Specific classes used only once.
class Dashboard(Reveals):
    def __init__(self, location: int, is_visible: bool, reveals: type(Base), name: str, location_text: str,
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
        self.reveals.is_visible = True
        # No items
        if not self.key and not self.power and not self.fuel:
            return f"{self.key_false}\n{self.power_false}\n{self.fuel_false}\n{self.description}"
        # Only key
        elif self.key and not self.power and not self.fuel:
            return f"{self.key_true}\n{self.power_false}\n{self.fuel_false}\n{self.description}"
        # Only power
        elif not self.key and self.power and not self.fuel:
            return f"{self.key_false}\n{self.power_true}\n{self.fuel_false}\n{self.description}"
        # Only fuel
        elif not self.key and not self.power and self.fuel:
            return f"{self.key_false}\n{self.power_false}\n{self.fuel_true}\n{self.description}"
        # Key and power
        elif self.key and self.power and not self.fuel:
            return f"{self.key_true}\n{self.power_true}\n{self.fuel_false}\n{self.description}"
        # Key and fuel
        elif self.key and not self.power and self.fuel:
            return f"{self.key_true}\n{self.power_false}\n{self.fuel_true}\n{self.description}"
        # Power and fuel
        elif not self.key and self.power and self.fuel:
            return f"{self.key_false}\n{self.power_true}\n{self.fuel_true}\n{self.description}"
        # Key, Power and Fuel
        elif self.key and self.power and self.fuel:
            return f"{self.key_true}\n{self.power_true}\n{self.fuel_true}\n{self.description}"
        else:
            return "An Error occurred with the DASHBOARD. Please Report"


class FinalButton(Base):
    def __init__(self, location, is_visible, name, location_text, description, inactive, active):
        super().__init__(location, is_visible, name, location_text, description)
        self.condition = False
        self.inactive = inactive
        self.active = active


class Compartment(Base):
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
            return f"{self.description}\n{self.battery_false}\n{self.power_cable_false}"
        elif not self.battery and self.cable:
            return f"{self.description}\n{self.battery_false}\n{self.power_cable_true}"
        elif self.battery and not self.cable:
            return f"{self.description}\n{self.battery_true}\n{self.power_cable_false}"
        elif self.battery and self.cable:
            return f"{self.description}\n{self.battery_true}\n{self.power_cable_true}"
        else:
            return "An Error occurred with the COMPARTMENT. Please Report"


class HeavyChest(Container):
    def __init__(self, location, is_visible, reveals, holds, locked, name, location_text, description, locked_text,
                 full, empty):
        super().__init__(location, is_visible, locked, name, location_text, description)
        self.reveals = reveals
        self.holds = holds
        self.locked_text = locked_text
        self.full = full
        self.empty = empty

    def inspect(self):
        self.reveals.is_visible = True
        if self.locked:
            return f"{self.description}\n{self.locked_text}"
        elif not self.locked:
            if not self.holds.moved:
                self.holds.is_visible = True
                return f"{self.description}\n{self.full}"
            elif self.holds.moved:
                return f"{self.description}\n{self.empty}"


class Keypad(Base):
    def __init__(self, location, is_visible, code, name, location_text, description):
        super().__init__(location, is_visible, name, location_text, description)
        self.code = code


# Specific consumable that can be refilled
class WaterBottle(Consumable):
    def __init__(self, location: int, is_visible: bool, food: int, drink: int, name, location_text: str,
                 description: str, consumed: str, empty: str):
        super().__init__(location, is_visible, food, drink, name, location_text, description, consumed)
        self.is_full = True
        self.empty = empty


# Specific reveals movable for the fruit trees, as six types of fruit.
class FruitTree(RevealsMovable):
    def __init__(self, location: int, is_visible: bool, reveals: list[type(Base)], name: str, location_text: str,
                 description: str, item_one_true: str, item_one_partial: str, item_one_false: str):
        super().__init__(location, is_visible, reveals, name, location_text, description, item_one_true, item_one_false)
        self.item_one_partial = item_one_partial

    def inspect(self):
        count = 0
        fruit_trees = ""
        for fruit in self.reveals:
            fruit.is_visible = True
            if not fruit.moved:
                count += 1
                fruit_trees += f"{fruit.location_text}\n"
        if count == 6:
            return f"{self.description}\n{self.item_one_true}\n{fruit_trees}"
        elif 0 < count < 6:
            return f"{self.description}\n{self.item_one_partial}\n{fruit_trees}"
        elif count == 0:
            return f"{self.description}\n{self.item_one_false}\n{fruit_trees}"
        else:
            return "***ERROR MESSAGE***"


class Note(Base):
    def __init__(self, location, is_visible, linked, name, location_text, description):
        super().__init__(location, is_visible, name, location_text, description)
        self.linked = linked

    def inspect(self):
        self.linked.condition_met = True
        return f"{self.description}"


class Coin(Base):
    def __init__(self, location: int, is_visible: bool, revealed_by: type(Base), name: str, location_text: str,
                 description: str):
        super().__init__(location, is_visible, name, location_text, description)
        self.revealed_by = revealed_by


class Block(Base):
    def __init__(self, location: int, is_visible: bool, name: str, location_text: str,
                 description: str):
        super().__init__(location, is_visible, name, location_text, description)
        self.slot_one = None
        self.slot_two = None
        self.slot_three = None

    def inspect(self):
        slots = [self.slot_one, self.slot_two, self.slot_three]
        description = self.description + "\n"
        for i, item in enumerate(slots, start=1):
            if item is None:
                description += f"Slot {i} is empty.\n"
            else:
                description += f"Slot {i} contains {item.name}.\n"
        return description
