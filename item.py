# A base item that all inherit off.
class Base:
    items = list()

    def __init__(self, initial_location: int, is_visible: bool, name: str, location_text: str, description_text: str):
        self._initial_location = initial_location
        self._is_visible = is_visible
        self._name = name
        self._location_text = location_text
        self._description_text = description_text
        self._is_discovered = False
        self.items.append(self)

    def get_location(self):
        return self._initial_location

    def get_visibility_status(self):
        return self._is_visible

    def make_visible(self):
        self._is_visible = True

    def make_invisible(self):
        self._is_visible = False

    def get_item_name(self):
        return self._name

    def get_name(self):
        return self._name

    def get_location_description_text(self):
        return self._location_text

    def inspect(self):
        return self._description_text

    def get_discovery_status(self):
        return self._is_discovered

    def item_discovered(self):
        self._is_discovered = True


# Container items.
class Container(Base):
    containers = list()

    def __init__(self, initial_location: int, is_visible: bool, locked_status: bool, name: str, location_text: str,
                 description_text: str):
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._locked_status = locked_status
        self._open = False
        self.containers.append(self)

    def get_locked_status(self):
        return self._locked_status

    def unlock_container(self):
        self._locked_status = False
        return f"{self.get_name()} unlocked"

    def open_container(self):
        self._open = True


# If an item requires a condition to be met before it can complete something.
class Conditional(Base):
    def __init__(self, initial_location: int, is_visible: bool, name: str, location_text: str, description_text: str):
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._condition_status = False

    def get_condition_status(self):
        return self._condition_status

    def condition_met(self):
        self._condition_status = True


# Movable items.
# Basic.
class Movable(Base):
    movable_items = list()

    def __init__(self, initial_location: int, is_visible: bool, name: str, location_text: str, description_text: str):
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._moved = False
        self.movable_items.append(self)

    def get_moved_status(self):
        return self._moved

    def item_moved(self):
        self._moved = True


# A movable item that has been revealed by another.
class RevealedMovable(Movable):
    def __init__(self, initial_location: int, is_visible: bool, revealed_by: type(Base), name: str, location_text: str,
                 description_text: str):
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self.revealed_by = revealed_by

    def get_item_revealed_by(self):
        return self.revealed_by


class ConditionalRevealedMovable(RevealedMovable, Conditional):
    def __init__(self, initial_location: int, is_visible: bool, revealed_by: type(Base), name: str, location_text: str,
                 description_text: str):
        super().__init__(initial_location, is_visible, revealed_by, name, location_text, description_text)


# Food items that can be consumed.
class Consumable(Movable):
    consumables = list()

    def __init__(self, initial_location: int, is_visible: bool, food_value: int, drink_value: int, name,
                 location_text: str, description_text: str, consumed_text: str):
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._food_value = food_value
        self._drink_value = drink_value
        self._consumed_text = consumed_text
        self.consumables.append(self)

    def inspect(self):
        return f"{self._description_text}\nFood: {self._food_value}   Drink: {self._drink_value}."

    def get_food_value(self):
        return self._food_value

    def get_drink_value(self):
        return self. _drink_value

    def item_consumed(self):
        return self._consumed_text


# A movable item that has been revealed by another.
class RevealedConsumable(Consumable):
    def __init__(self, initial_location: int, is_visible: bool, food_value: int, drink_value: int,
                 revealed_by: type(Base), name: str, location_text: str, description_text: str, consumed_text):
        super().__init__(initial_location, is_visible, food_value, drink_value, name, location_text, description_text,
                         consumed_text)
        self.revealed_by = revealed_by

    def get_item_revealed_by(self):
        return self.revealed_by


# An item that when inspected, reveals another.
# Basic.
class Reveals(Base):
    def __init__(self, initial_location: int, is_visible: bool, reveals: type(Base), name: str, location_text: str,
                 description_text: str):
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._reveals = reveals

    def inspect(self):
        self._reveals.make_visible()
        return self._description_text

    def get_revealed_item(self):
        return self._reveals


# If there is a condition before the item reveals another.
class ConditionalReveals(Reveals, Conditional):
    def __init__(self, initial_location: int, is_visible: bool, reveals: type(Base), name: str, location_text: str,
                 description_text: str, reveal_text: str):
        super().__init__(initial_location, is_visible, reveals, name, location_text, description_text)
        self._reveal_text = reveal_text

    def inspect(self):
        self._reveals.make_visible()
        if not self.get_condition_status():
            return self._description_text
        elif self.get_condition_status():
            return self._reveal_text
        else:
            return "An error has occurred. Please report this to the game design team."

    def get_reveal_text(self):
        return self._reveal_text


# If the item reveals a movable item.
class RevealsMovable(Reveals):
    def __init__(self, initial_location: int, is_visible: bool, reveals: type(Base), name: str, location_text: str,
                 description_text: str, item_one_true_text: str, item_one_false_text: str):
        super().__init__(initial_location, is_visible, reveals, name, location_text, description_text)
        self._item_one_status = False
        self._item_one_true_text = item_one_true_text
        self._item_one_false_text = item_one_false_text

    def inspect(self):
        self._reveals.get_visibility_status()
        if not self.is_item_one_taken():
            return f"{self._description_text}\n{self._item_one_true_text}"
        elif self.is_item_one_taken():
            return self._item_one_false_text
        else:
            return "An error has occurred. Please report this to the game design team."

    def is_item_one_taken(self):
        return self._item_one_status

    def item_one_taken(self):
        self._item_one_status = True


# If a condition must be met before a movable item is revealed.
class ConditionalRevealsMovable(RevealsMovable, Conditional):
    def __init__(self, initial_location: int, is_visible: bool, reveals: type(Base), name: str, location_text: str,
                 description_text: str, item_one_true_text: str, item_one_false_text: str):
        super().__init__(initial_location, is_visible, reveals, name, location_text, description_text,
                         item_one_true_text, item_one_false_text)

    def inspect(self):
        if not self._condition_status:
            return f"{self._description_text}\n{self._item_one_false_text}"
        elif self._condition_status and not self._item_one_status:
            self._reveals._is_visible = True
            return f"{self._description_text}\n{self._item_one_true_text}"
        elif self._condition_status and self._item_one_status:
            return f"{self._description_text}\n{self._item_one_false_text}"
        else:
            return "An error has occurred. Please report this to the game design team."


# If the item reveals two movable items.
class DualRevealsMovable(RevealsMovable):
    def __init__(self, initial_location: int, is_visible: bool, reveals: list[type(Base)], name: str,
                 location_text: str, description_text: str, item_one_true_text: str, item_one_false_text: str,
                 item_two_true_text: str, item_two_false_text: str):
        super().__init__(initial_location, is_visible, reveals, name, location_text, description_text,
                         item_one_true_text, item_one_false_text)
        self._item_two_status = False
        self._item_two_true_text = item_two_true_text
        self._item_two_false_text = item_two_false_text

    def inspect(self):
        for item in self._reveals:
            item.make_visible()
        if not self.is_item_one_taken() and not self.is_item_two_taken():
            return f"{self._description_text}\n{self._item_one_true_text}\n{self._item_two_true_text}"
        elif not self.is_item_one_taken() and self.is_item_two_taken:
            return f"{self._description_text}\n{self._item_one_true_text}\n{self._item_two_false_text}"
        elif self.is_item_one_taken() and not self.is_item_two_taken:
            return f"{self._description_text}\n{self._item_one_false_text}\n{self._item_two_true_text}"
        elif self.is_item_one_taken() and self.is_item_two_taken:
            return f"{self._description_text}\n{self._item_one_false_text}\n{self._item_two_false_text}"
        else:
            return "An error has occurred. Please report this to the game design team."

    def is_item_two_taken(self):
        return self._item_two_status

    def item_two_taken(self):
        self._item_two_status = True


# If the item requires something to be inserted.
class RequiresInsert(Base):
    def __init__(self, initial_location: int, is_visible: bool, name: str, location_text: str, description_text: str,
                 full_text: str):
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._insert = False
        self._full_text = full_text

    def inspect(self):
        if not self.insert_status():
            return self._description_text
        elif self.insert_status():
            return self._full_text
        else:
            return "An error has occurred. Please report this to the game design team."

    def insert_status(self):
        return self._insert

    def item_inserted(self):
        self._insert = True

    def get_full_text(self):
        return self._full_text


# Non Player Characters.
class Npc(Base):
    def __init__(self, initial_location: int, is_visible: bool, name: str, location_text: str, description_text: str,
                 initial_text: str):
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._initial_text = initial_text

    def get_initial_dialogue(self):
        return self._initial_text


# Specific classes used only once.
class Dashboard(Reveals):
    def __init__(self, initial_location: int, is_visible: bool, reveals: type(Base), name: str, location_text: str,
                 description_text: str, key_false_text: str, key_true_text: str, power_false_text: str,
                 power_true_text: str, fuel_false_text: str, fuel_true_text: str):
        super().__init__(initial_location, is_visible, reveals, name, location_text, description_text)
        self.reveals = reveals
        self._key_false_text = key_false_text
        self._key_true_text = key_true_text
        self._power_false_text = power_false_text
        self._power_true_text = power_true_text
        self._fuel_false_text = fuel_false_text
        self._fuel_true_text = fuel_true_text
        self._key = False
        self._power = False
        self._fuel = False

    def inspect(self):
        self.reveals.check_visibility()
        # No items
        if not self.get_key_status() and not self.get_power_status() and not self.get_fuel_status():
            return f"{self._key_false_text}\n{self._power_false_text}\n{self._fuel_false_text}\n{self._description_text}"
        # Only key
        elif self.get_key_status() and not self.get_power_status() and not self.get_fuel_status():
            return f"{self._key_true_text}\n{self._power_false_text}\n{self._fuel_false_text}\n{self._description_text}"
        # Only power
        elif not self.get_key_status() and self.get_power_status() and not self.get_fuel_status():
            return f"{self._key_false_text}\n{self._power_true_text}\n{self._fuel_false_text}\n{self._description_text}"
        # Only fuel
        elif not self.get_key_status() and not self.get_power_status() and self.get_fuel_status():
            return f"{self._key_false_text}\n{self._power_false_text}\n{self._fuel_true_text}\n{self._description_text}"
        # Key and power
        elif self.get_key_status() and self.get_power_status() and not self.get_fuel_status():
            return f"{self._key_true_text}\n{self._power_true_text}\n{self._fuel_false_text}\n{self._description_text}"
        # Key and fuel
        elif self.get_key_status() and not self.get_power_status() and self.get_fuel_status():
            return f"{self._key_true_text}\n{self._power_false_text}\n{self._fuel_true_text}\n{self._description_text}"
        # Power and fuel
        elif not self.get_key_status() and self.get_power_status() and self.get_fuel_status():
            return f"{self._key_false_text}\n{self._power_true_text}\n{self._fuel_true_text}\n{self._description_text}"
        # Key, Power and Fuel
        elif self.get_key_status() and self.get_power_status() and self.get_fuel_status():
            return f"{self._key_true_text}\n{self._power_true_text}\n{self._fuel_true_text}\n{self._description_text}"
        else:
            return "An error has occurred. Please report this to the game design team."

    def get_key_status(self):
        return self._key

    def key_inserted(self):
        self._key = True

    def get_key_true_text(self):
        return self._key_true_text

    def get_power_status(self):
        return self._power

    def dashboard_powered(self):
        self._power = True

    def get_fuel_status(self):
        return self._fuel

    def boat_fueled(self):
        self._fuel = True


class FinalButton(Conditional):
    def __init__(self, initial_location: int, is_visible: bool, name: str, location_text: str, description_text: str,
                 inactive_text: str):
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._inactive_text = inactive_text

    def get_inactive_button_text(self):
        return self._inactive_text


class Compartment(Base):
    def __init__(self, initial_location: int, is_visible: bool, name: str, location_text: str,
                 description_text: str, battery_false_text: str, battery_true_text: str, power_cable_false_text: str,
                 power_cable_true_text: str):
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._battery_false_text = battery_false_text
        self._battery_true_text = battery_true_text
        self._power_cable_false_text = power_cable_false_text
        self._power_cable_true_text = power_cable_true_text
        self._battery_status = False
        self._cable_status = False

    def inspect(self):
        if not self.get_battery_status() and not self.get_cable_status():
            return f"{self._description_text}\n{self._battery_false_text}\n{self._power_cable_false_text}"
        elif not self.get_battery_status() and self.get_cable_status():
            return f"{self._description_text}\n{self._battery_false_text}\n{self._power_cable_true_text}"
        elif self.get_battery_status() and not self.get_cable_status():
            return f"{self._description_text}\n{self._battery_true_text}\n{self._power_cable_false_text}"
        elif self.get_battery_status() and self.get_cable_status():
            return f"{self._description_text}\n{self._battery_true_text}\n{self._power_cable_true_text}"
        else:
            return "An error has occurred. Please report this to the game design team."

    def get_battery_status(self):
        return self._battery_status

    def battery_inserted(self):
        self._battery_status = True

    def get_battery_true_text(self):
        return self._battery_true_text

    def get_cable_status(self):
        return self._cable_status

    def cable_inserted(self):
        self._cable_status = True


class HeavyChest(Container):
    def __init__(self, initial_location: int, is_visible: bool, reveals: type(Base), holds: type(Base),
                 locked_status: bool, name: str, location_text: str, description_text: str, locked_text: str,
                 full_text: str, empty_text: str):
        super().__init__(initial_location, is_visible, locked_status, name, location_text, description_text)
        self._reveals = reveals
        self._holds = holds
        self._locked_text = locked_text
        self._full_text = full_text
        self._empty_text = empty_text

    def inspect(self):
        self._reveals.get_visibility_status()
        if self.get_locked_status():
            return f"{self._description_text}\n{self._locked_text}"
        elif not self.get_locked_status():
            if not self._holds.get_moved_status():
                self._holds.make_visible()
                return f"{self._description_text}\n{self._full_text}"
            elif self._holds.get_moved_status():
                return f"{self._description_text}\n{self._empty_text}"


class Keypad(Base):
    def __init__(self, initial_location: int, is_visible: bool, access_code: str, name: str, location_text: str,
                 description_text: str):
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._access_code = access_code

    def get_access_code(self):
        return self._access_code


# Specific consumable that can be refilled
class WaterBottle(Consumable):
    def __init__(self, initial_location: int, is_visible: bool, food_value: int, drink_value: int, name,
                 location_text: str, description_text: str, consumed_text: str, empty_text: str):
        super().__init__(initial_location, is_visible, food_value, drink_value, name, location_text, description_text,
                         consumed_text)
        self._is_full = True
        self._empty_text = empty_text

    def get_water_bottle_status(self):
        return self._is_full

    def fill_water_bottle(self):
        self._is_full = True
        return "You fill up your water bottle."

    def empty_water_bottle(self):
        self._is_full = False


# Specific reveals movable for the fruit trees, as six types of fruit.
class FruitTree(RevealsMovable):
    def __init__(self, initial_location: int, is_visible: bool, reveals: list[type(Base)], name: str,
                 location_text: str, description_text: str, item_one_true_text: str, item_one_partial_text: str,
                 item_one_false_text: str):
        super().__init__(initial_location, is_visible, reveals, name, location_text, description_text,
                         item_one_true_text, item_one_false_text)
        self._item_one_partial_text = item_one_partial_text

    def inspect(self):
        count = 0
        fruit_trees = ""
        for fruit in self._reveals:
            fruit.get_visibility_status()
            if not fruit.get_moved_status():
                count += 1
                fruit_trees += f"{fruit.get_location_description_text()}\n"
        if count == 6:
            return f"{self._description_text}\n{self._item_one_true_text}\n{fruit_trees}"
        elif 0 < count < 6:
            return f"{self._description_text}\n{self._item_one_partial_text}\n{fruit_trees}"
        elif count == 0:
            return f"{self._description_text}\n{self._item_one_false_text}\n{fruit_trees}"
        else:
            return "An error has occurred. Please report this to the game design team."


class Note(Base):
    def __init__(self, initial_location: int, is_visible: bool, linked: type(Conditional), name: str,
                 location_text: str, description_text: str):
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self.linked = linked

    def inspect(self):
        self.linked.condition_met()
        return f"{self._description_text}"


class Coin(Base):
    def __init__(self, initial_location: int, is_visible: bool, revealed_by: type(Base), name: str, location_text: str,
                 description_text: str):
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self.revealed_by = revealed_by


class Block(Base):
    def __init__(self, initial_location: int, is_visible: bool, name: str, location_text: str,
                 description_text: str):
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._slot_one_item = None
        self._slot_two_item = None
        self._slot_three_item = None

    def inspect(self):
        slots = self.list_slot_items()
        description = self._description_text + "\n"
        for i, item in enumerate(slots, start=1):
            if item is None:
                description += f"Slot {i} is empty.\n"
            else:
                description += f"Slot {i} contains {item.get_name()}.\n"
        return description

    def get_slot_items(self):
        slots = self.list_slot_items()
        description = ""
        for i, item in enumerate(slots, start=1):
            if item is None:
                description += f"Slot {i} is empty.\n"
            else:
                description += f"Slot {i} contains {item.get_name()}.\n"
        return description

    def get_slot_one_item(self):
        return self._slot_one_item

    def set_slot_one_item(self, item):
        self._slot_one_item = item

    def get_slot_two_item(self):
        return self._slot_two_item

    def set_slot_two_item(self, item):
        self._slot_two_item = item

    def get_slot_three_item(self):
        return self._slot_three_item

    def set_slot_three_item(self, item):
        self._slot_three_item = item

    def list_slot_items(self):
        return [self.get_slot_one_item(), self.get_slot_two_item(), self.get_slot_three_item()]
