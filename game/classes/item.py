class Item:
    """
    This class represents a generic item that all other will inherit off.
    It keeps track of all created items classes.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the item spawn.
        _is_visible (bool): Whether the item can initially be seen or not.
        _name (str): The name of the item.
        _location_text (str): A description of where the item is located.
        _description_text (str): A description of the item.
        _discovery_status (bool): Has the player discovered the item.
        nouns (list): A list of all item classes.
    """
    items = list()

    def __init__(self, initial_location: int, is_visible: bool, name: str, location_text: str, description_text: str):
        """
        Initialize a new item.
        :param initial_location: The unique ID of the location the item spawns.
        :param is_visible: Whether the item can initially be seen or not.
        :param name: The name of the item.
        :param location_text: A description of where the item is located.
        :param description_text: A description of the item.
        """
        self._initial_location = initial_location
        self._is_visible = is_visible
        self._name = name
        self._location_text = location_text
        self._description_text = description_text
        self._discovery_status = False
        self.items.append(self)

    def get_initial_location_id(self):
        """
        Gets the unique ID of the location the item spawns.
        :return: The items initial locations unique ID.
        """
        return self._initial_location

    def get_visibility_status(self):
        """
        Gets the current visibility status of the item.
        :return: The visibility status.
        """
        return self._is_visible

    def make_visible(self):
        """
        Set the item to be visible.
        """
        self._is_visible = True

    def make_invisible(self):
        """
        Set the item to be invisible.
        """
        self._is_visible = False

    def get_name(self):
        """
        Gets the name of the item.
        :return: The name.
        """
        return self._name

    def get_location_description_text(self):
        """
        Gets the description of where the item is located.
        :return: The description.
        """
        return self._location_text

    def set_location_description_text(self, text):
        """
        Sets the description of where the item is located.
        """
        self._location_text = text

    def get_description_text(self):
        """
        Gets the description of the item.
        :return: The description.
        """
        return self._description_text

    def set_description_text(self, description):
        """
        Sets the description of the item.
        """
        self._description_text = f"On the paper is a cryptic clue.\n'{description}'"

    def get_discovery_status(self):
        """
        Gets the current discovery status of the item.
        :return: The discovery status.
        """
        return self._discovery_status

    def item_discovered(self):
        """
        Sets the discovery status to True when the item is discovered.
        """
        self._discovery_status = True

    def inspect(self):
        """
        A general inspect, for when the player wants more information on an item.
        :return: The description of the item.
        """
        return self.get_description_text()


class Container(Item):
    """
    This class represents a container that can unlocked and opened.
    It inherits off item.
    It keeps track of all created container classes.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the container spawns.
        _is_visible (bool): Whether the container can initially be seen or not.
        _reveals_item type(Item) or None: If the container reveals another item initially.
        _holds_item: type(Item): The item the container holds inside.
        _locked_status (bool): Whether the container is lock or not.
        _name (str): The name of the container.
        _location_text (str): A description of where the container is located.
        _description_text (str): A description of the container.
        _full_text (str): A description when the container is full.
        _empty_text (str): A description when the container is empty.
        _discovery_status (bool): Has the player discovered the container.
        _open_status (bool): Whether the container is open or not.
        container_nouns (list): A list of all container item classes.
    """
    containers = list()

    def __init__(self, initial_location: int, is_visible: bool, reveals: type(Item) or None, holds: type(Item),
                 locked_status: bool, name: str, location_text: str, description_text: str, full_text: str,
                 empty_text: str):
        """
        Initialize a new container item.
        :param initial_location: The unique ID of the location the container spawns.
        :param is_visible: Whether the container can initially be seen or not.
        :param reveals: If the container reveals another item initially, otherwise None.
        :param holds: The item the container holds inside.
        :param locked_status: Whether the container is lock or not.
        :param name: The name of the container.
        :param location_text: A description of where the container is located.
        :param description_text: A description of the container.
        :param full_text: A description when the container is full.
        :param empty_text: A description when the container is empty.
        """
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._locked_status = locked_status
        self._reveals_item = reveals
        self._holds_item = holds
        self._full_text = full_text
        self._empty_text = empty_text
        self._open_status = False
        self.containers.append(self)

    def inspect(self):
        """
        Overrides Inspect()
        Returns a different string depending on if the container is still locked, not opened, full or empty.
        :return: The string.
        """
        if self.get_revealed_item() is not None:
            self.get_revealed_item().make_visible()

        if self.get_locked_status():
            return f"{self.get_description_text()}\nIt's Locked."
        elif not self.get_open_status():
            return f"{self.get_description_text()}\nIt's Closed."
        else:
            if self.get_holds_item() is not None:
                self.get_holds_item().make_visible()
                return f"{self.get_description_text()}\n{self.get_full_container_text()}"
            else:
                return f"{self.get_description_text()}\n{self.get_empty_container_text()}"

    def set_revealed_item(self, item):
        """
        Sets the revealed item.
        :param item: Item to be revealed.
        """
        self._reveals_item = item

    def get_revealed_item(self):
        """
        Gets the item that the container reveals.
        :return: The noun.
        """
        return self._reveals_item

    def set_holds_item(self, item):
        """
        Sets the item the container holds.
        :param item: Item the container holds.
        """
        self._holds_item = item

    def get_holds_item(self):
        """
        Gets the item that is inside the container.
        :return: The noun.
        """
        return self._holds_item

    def get_full_container_text(self):
        """
        Gets the description when the container is full.
        :return: The description.
        """
        return self._full_text

    def get_empty_container_text(self):
        """
        Gets the description when the container is empty.
        :return: The description.
        """
        return self._empty_text

    def get_locked_status(self):
        """
        Gets the current locked status of the container.
        :return: The locked status.
        """
        return self._locked_status

    def unlock_container(self):
        """
        Sets the locked status of the container to False and returns a string saying so.
        :return: The container unlocked.
        """
        self._locked_status = False
        return f"{self.get_name()} unlocked."

    def get_open_status(self):
        """
        Gets the current open status of the container.
        :return: The open status.
        """
        return self._open_status

    def open_container(self):
        """
        Sets the open status of the container to True and returns a string saying so.
        :return: The container opened.
        """
        self._open_status = True
        if self.get_holds_item() is not None:
            self.get_holds_item().make_visible()
        return f"{self.get_name()} opened.\n{self.get_full_container_text()}"

    def item_one_taken(self):
        """
        Sets the hold item to None once it is taken.
        """
        self.set_holds_item(None)


class Conditional(Item):
    """
    This class represents a conditional item that can only been seen and/or taken after an event has occurred.
    It inherits off item.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the item spawns.
        _is_visible (bool): Whether the item can initially be seen or not.
        _name (str): The name of the item.
        _location_text (str): A description of where the item is located.
        _description_text (str): A description of the item.
        _discovery_status (bool): Has the player discovered the item.
        _condition_status (bool): Has the condition been met for another event can take place.
    """
    def __init__(self, initial_location: int, is_visible: bool, name: str, location_text: str, description_text: str):
        """
        Initialize a new conditional item.
        :param initial_location: The unique ID of the location the item spawns.
        :param is_visible: Whether the item can initially be seen or not.
        :param name: The name of the item.
        :param location_text: A description of where the item is located.
        :param description_text: A description of the item.
        """
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._condition_status = False

    def get_condition_status(self):
        """
        Gets the current conditional status of the item.
        :return: The conditional status.
        """
        return self._condition_status

    def condition_met(self):
        """
        Sets the conditional status to True.
        """
        self._condition_status = True


class Movable(Item):
    """
    This class represents a generic movable item that can be picked up and moved.
    It inherits off item.
    It keeps track of all created movable item classes.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the item spawns.
        _is_visible (bool): Whether the item can initially be seen or not.
        _name (str): The name of the item.
        _location_text (str): A description of where the item is located.
        _description_text (str): A description of the item.
        _discovery_status (bool): Has the player discovered the item.
        _moved_status (bool): Has the item been picked up by the player.
        movable_nouns (list): A list of all movable item classes.
    """
    movable_nouns = list()

    def __init__(self, initial_location: int, is_visible: bool, name: str, location_text: str, description_text: str):
        """
        Initialize a new movable item.
        :param initial_location: The unique ID of the location the item first appears in.
        :param is_visible: Whether the item can initially be seen or not.
        :param name: The name of the item.
        :param location_text: A description of where the item is located.
        :param description_text: A description of the item.
        """
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._moved_status = False
        self.movable_nouns.append(self)

    def get_moved_status(self):
        """
        Gets the current moved status of the item.
        :return: The moved status.
        """
        return self._moved_status

    def item_moved(self):
        """
        Sets the moved status to True.
        """
        self._moved_status = True


class RevealedMovable(Movable):
    """
    This class represents a movable item that has been revealed by another item.
    It inherits off movable.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the item spawns.
        _is_visible (bool): Whether the item can initially be seen or not.
        _revealed_by (type(Item)): The item that reveals movable noun.
        _name (str): The name of the item.
        _location_text (str): A description of where the item is located.
        _description_text (str): A description of the item.
        _discovery_status (bool): Has the player discovered the item.
        _moved_status (bool): Has the item been picked up by the player.
    """
    def __init__(self, initial_location: int, is_visible: bool, revealed_by: type(Item), name: str, location_text: str,
                 description_text: str):
        """
        Initialize a new revealed movable item.
        :param initial_location: The unique ID of the location the item spawns.
        :param is_visible: Whether the item can initially be seen or not.
        :param revealed_by: The item that reveals the movable noun.
        :param name: The name of the item.
        :param location_text: A description of where the item is located.
        :param description_text: A description of the item.
        """
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._revealed_by = revealed_by

    def get_item_revealed_by(self):
        """
        Gets the item that revealed the item.
        :return: The revealing noun.
        """
        return self._revealed_by


class ConditionalRevealedMovable(RevealedMovable, Conditional):
    """
    This class represents a revealed movable item that can only been seen and/or taken after an event has occurred.
    It inherits off revealed movable and conditional.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the item spawns.
        _is_visible (bool): Whether the item can initially be seen or not.
        _revealed_by (type(Item)): The item that reveals movable noun.
        _name (str): The name of the item.
        _location_text (str): A description of where the item is located.
        _description_text (str): A description of the item.
        _discovery_status (bool): Has the player discovered the item.
        _moved_status (bool): Has the item been picked up by the player.
        _condition_status (bool): Has the condition been met for another event can take place.
    """
    def __init__(self, initial_location: int, is_visible: bool, revealed_by: type(Item), name: str, location_text: str,
                 description_text: str):
        """
        Initialize a new conditionally revealed movable item.
        :param initial_location: The unique ID of the location the noun item spawns.
        :param is_visible: Whether the item can initially be seen or not.
        :param revealed_by: The item that reveals the movable item.
        :param name: The name of the item.
        :param location_text: A description of where the item is located.
        :param description_text: A description of the item.
        """
        super().__init__(initial_location, is_visible, revealed_by, name, location_text, description_text)


class Consumable(Movable):
    """
    This class represents a generic consumable item that can be consumed for energy and hydration.
    It inherits off movable.
    It keeps track of all created consumable item classes.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the consumable spawns.
        _is_visible (bool): Whether the consumable can initially be seen or not.
        _energy_value (int): The value of energy points gained from consuming the consumable.
        _hydration_value (int): The value of hydration points gained from consuming the consumable.
        _name (str): The name of the consumable.
        _location_text (str): A description of where the consumable is located.
        _description_text (str): A description of the consumable.
        _consumed_text (str): A description of eating the consumable.
        _discovery_status (bool): Has the player discovered the consumable.
        _moved_status (bool): Has the consumable been picked up by the player.
        consumable_nouns (list): A list of all consumable noun classes.
    """
    consumable_nouns = list()

    def __init__(self, initial_location: int, is_visible: bool, energy_value: int, hydration_value: int, name,
                 location_text: str, description_text: str, consumed_text: str):
        """
        Initialize a new consumable item.
        :param initial_location: The unique ID of the location the consumable spawns.
        :param is_visible: Whether the consumable can initially be seen or not.
        :param energy_value: The value of energy points gained from consuming the consumable.
        :param hydration_value: The value of hydration points gained from consuming the consumable.
        :param name: The name of the consumable.
        :param location_text: A description of where the consumable is located.
        :param description_text: A description of the consumable.
        :param consumed_text: A description of eating the consumable.
        """
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._energy_value = energy_value
        self._hydration_value = hydration_value
        self._consumed_text = consumed_text
        self.consumable_nouns.append(self)

    def inspect(self):
        """
        Overrides Inspect()
        Changes the description to include unknown stats.
        :return: The description.
        """
        return f"{self.get_description_text()}\nFood: Unknown   Drink: Unknown"

    def intelligent_inspect(self):
        """
        Creates a string showing the description as well as the energy and hydration values.
        :return: The string
        """
        return f"{self.get_description_text()}\nFood: {self.get_energy_value()}   Drink: {self.get_hydration_value()}"

    def get_energy_value(self):
        """
        Gets the energy points gained from consuming the consumable.
        :return: The energy points.
        """
        return self._energy_value

    def get_hydration_value(self):
        """
        Gets the hydration points gained from consuming the consumable.
        :return: The hydration points.
        """
        return self. _hydration_value

    def item_consumed(self):
        """
        Gets the eating description of the consumable.
        :return: The description.
        """
        return self._consumed_text


class RevealedConsumable(Consumable):
    """
    This class represents a revealed consumable item that can be consumed for energy and hydration
    It inherits off consumable.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the consumable spawns.
        _is_visible (bool): Whether the consumable can initially be seen or not.
        _energy_value (int): The value of energy points gained from consuming the consumable.
        _hydration_value (int): The value of hydration points gained from consuming the consumable.
        _revealed_by (type(Noun)): The noun that reveals the consumable.
        _name (str): The name of the consumable.
        _location_text (str): A description of where the consumable is located.
        _description_text (str): A description of the consumable.
        _consumed_text (str): A description of eating the consumable.
        _discovery_status (bool): Has the player discovered the consumable.
        _moved_status (bool): Has the consumable been picked up by the player.
    """
    def __init__(self, initial_location: int, is_visible: bool, energy_value: int, hydration_value: int,
                 revealed_by: type(Item), name: str, location_text: str, description_text: str, consumed_text):
        """
        Initialize a new revealed consumable item.
        :param initial_location: The unique ID of the location the consumable spawns.
        :param is_visible: Whether the consumable can initially be seen or not.
        :param energy_value: The value of energy points gained from consuming the consumable.
        :param hydration_value: The value of hydration points gained from consuming the consumable.
        :param revealed_by: The noun that reveals the consumable.
        :param name: The name of the consumable.
        :param location_text: A description of where the consumable is located.
        :param description_text: A description of the consumable.
        :param consumed_text: A description of eating the consumable.
        """
        super().__init__(initial_location, is_visible, energy_value, hydration_value, name, location_text,
                         description_text, consumed_text)
        self._revealed_by = revealed_by

    def get_item_revealed_by(self):
        """
        Gets the item that revealed the consumable.
        :return: The revealing noun.
        """
        return self._revealed_by

    def set_energy_value(self, value):
        """
        Sets the energy value of the consumable to the given value.
        """
        self._energy_value = value

    def set_hydration_value(self, value):
        """
        Sets the hydration value of the consumable to the given value.
        """
        self._hydration_value = value

    def set_consumed_text(self, text):
        """
        Sets the consumed text of the consumable to the given text.
        """
        self._consumed_text = text


class Reveals(Item):
    """
    This class represents a generic reveals item that reveals another item.
    It inherits off item.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the item spawns.
        _is_visible (bool): Whether the item can initially be seen or not.
        _reveals_item (type(Item)): The item that this item reveals.
        _name (str): The name of the item.
        _location_text (str): A description of where the item is located.
        _description_text (str): A description of the item.
        _discovery_status (bool): Has the player discovered the item.
    """
    def __init__(self, initial_location: int, is_visible: bool, reveals: type(Item), name: str, location_text: str,
                 description_text: str):
        """
        Initialize a new reveals noun.
        :param initial_location: The unique ID of the location the item spawns.
        :param is_visible: Whether the item can initially be seen or not.
        :param reveals: The item that this item reveals.
        :param name: The name of the item.
        :param location_text: A description of where the item is located.
        :param description_text: A description of the item.
        """
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._reveals_item = reveals

    def inspect(self):
        """
        Overrides Inspect()
        Gets the item it reveals and makes it visible
        :return: The description of the noun.
        """
        self.get_revealed_item().make_visible()
        return self.get_description_text()

    def get_revealed_item(self):
        """
        Gets the item that this item reveals.
        :return: The noun.
        """
        return self._reveals_item

    def set_revealed_item(self, item):
        """
        Sets the revealed item.
        :param item: Item to be revealed.
        """
        self._reveals_item = item


class ConditionalReveals(Reveals, Conditional):
    """
    This class represents a conditional reveals item that reveals another item if a condition is met.
    It inherits off reveals and conditional.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the item spawns.
        _is_visible (bool): Whether the item can initially be seen or not.
        _reveals_item (type(Item)): The item that this item reveals.
        _name (str): The name of the item.
        _location_text (str): A description of where the item is located before the condition is met.
        _description_text (str): A description of the item.
        _reveal_text (str): A description of where the item is located after the condition is met.
        _discovery_status (bool): Has the player discovered the item.
        _condition_status (bool): Has the condition been met for another event can take place.
    """
    def __init__(self, initial_location: int, is_visible: bool, reveals: type(Item), name: str, location_text: str,
                 description_text: str, reveal_text: str):
        """
        Initialize a new conditionally reveals item.
        :param initial_location: The unique ID of the location the item spawns.
        :param is_visible: Whether the item can initially be seen or not.
        :param reveals: The item that this item reveals.
        :param name: The name of the item.
        :param location_text: A description of where the item is located.
        :param description_text: A description of the item.
        :param reveal_text: A description of where the item is located after the condition is met.
        """
        super().__init__(initial_location, is_visible, reveals, name, location_text, description_text)
        self._reveal_text = reveal_text

    def inspect(self):
        """
        Overrides Inspect()
        Once the conditional status is met, makes the item it reveals visible and returns the revealed text.
        :return: A description based on condition status.
        """
        if not self.get_condition_status():
            return self.get_description_text()
        else:
            self.get_revealed_item().make_visible()
            return self.get_reveal_text()

    def get_reveal_text(self):
        """
        Gets the text description once the item is revealed.
        :return: The description.
        """
        return self._reveal_text


class RevealsMovable(Reveals):
    """
    This class represents an item that reveals a movable item.
    It inherits off reveals.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the item spawns.
        _is_visible (bool): Whether the item can initially be seen or not.
        _reveals_item (type(Item)): The item that this item reveals.
        _name (str): The name of the item.
        _location_text (str): A description of where the item is located.
        _description_text (str): A description of the item.
        _item_one_true_text (str): An extension of the description if the item it reveals is there.
        _item_one_false_text (str): An extension of the description if the item it reveals is no longer there.
        _item_one_taken_status (bool): The status on if the item has been taken or not.
        _discovery_status (bool): Has the player discovered the item.
    """
    def __init__(self, initial_location: int, is_visible: bool, reveals: type(Item), name: str, location_text: str,
                 description_text: str, item_one_true_text: str, item_one_false_text: str):
        """
        Initialize a new reveals movable item.
        :param initial_location: The unique ID of the location the item spawns.
        :param is_visible: Whether the item can initially be seen or not.
        :param reveals: The item that this item reveals.
        :param name: The name of the item.
        :param location_text: A description of where the item is located.
        :param description_text: A description of the item.
        :param item_one_true_text: An extension of the description if the item it reveals is there.
        :param item_one_false_text: An extension of the description if the item it reveals is no longer there.
        """
        super().__init__(initial_location, is_visible, reveals, name, location_text, description_text)
        self._item_one_true_text = item_one_true_text
        self._item_one_false_text = item_one_false_text
        self._item_one_taken_status = False

    def inspect(self):
        """
        Overrides Inspect()
        Makes the item it reveals visible and returns a description based on whether the item has been taken or not.
        :return: A description based on taken status.
        """
        self.get_revealed_item().make_visible()
        if not self.get_item_one_taken_status():
            return f"{self.get_description_text()}\n{self.get_item_one_true_text()}"
        else:
            return f"{self.get_description_text()}\n{self.get_item_one_false_text()}"

    def get_item_one_true_text(self):
        """
        Gets the extra text description if the item is there.
        :return: The extra description.
        """
        return self._item_one_true_text

    def get_item_one_false_text(self):
        """
        Gets the extra text description if the item is not there.
        :return: The extra description.
        """
        return self._item_one_false_text

    def get_item_one_taken_status(self):
        """
        Gets the status on if the item has been taken or not.
        :return: The status.
        """
        return self._item_one_taken_status

    def item_one_taken(self):
        """
        Sets the status to True once the item is taken.
        """
        self._item_one_taken_status = True


class ConditionalRevealsMovable(RevealsMovable, Conditional):
    """
    This class represents a conditional reveals item that reveals a movable item if a condition is met.
    It inherits off reveals movable and conditional.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the item spawns.
        _is_visible (bool): Whether the item can initially be seen or not.
        _reveals_item (type(Item)): The item that this item reveals.
        _name (str): The name of the item.
        _location_text (str): A description of where the item is located.
        _description_text (str): A description of the item.
        _item_one_true_text (str): An extension of the description if the item it reveals is there.
        _item_one_false_text (str): An extension of the description if the item it reveals is no longer there.
        _item_one_taken (bool): The status on if the item has been taken or not.
        _discovery_status (bool): Has the player discovered the item.
    """
    def __init__(self, initial_location: int, is_visible: bool, reveals: type(Item), name: str, location_text: str,
                 description_text: str, item_one_true_text: str, item_one_false_text: str):
        """
        Initialize a new conditionally reveals movable item.
        :param initial_location: The unique ID of the location the item spawns.
        :param is_visible: Whether the item can initially be seen or not.
        :param reveals: The item that this item reveals.
        :param name: The name of the item.
        :param location_text: A description of where the item is located.
        :param description_text: A description of the item.
        :param item_one_true_text: An extension of the description if the item it reveals is there.
        :param item_one_false_text: An extension of the description if the item it reveals is no longer there.
        """
        super().__init__(initial_location, is_visible, reveals, name, location_text, description_text,
                         item_one_true_text, item_one_false_text)

    def inspect(self):
        """
        Overrides Inspect()
        Reveals the item once the condition has been met.
        Returns a description based on if the condition has been met and if the item has been taken.
        :return: A description.
        """
        if not self.get_condition_status():
            return f"{self.get_description_text()}\n{self.get_item_one_false_text()}"
        elif self.get_condition_status() and not self.get_item_one_taken_status():
            self.get_revealed_item().make_visible()
            return f"{self.get_description_text()}\n{self.get_item_one_true_text()}"
        elif self.get_condition_status() and self.get_item_one_taken_status():
            return f"{self.get_description_text()}\n{self.get_item_one_false_text()}"


class DualRevealsMovable(RevealsMovable):
    """
    This class represents an item that reveals two movable items
    It inherits off reveals movable.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the item spawns.
        _is_visible (bool): Whether the item can initially be seen or not.
        _reveals_item (type(Item)): The item that this item reveals.
        _name (str): The name of the item.
        _location_text (str): A description of where the item is located.
        _description_text (str): A description of the item.
        _item_one_true_text (str): An extension of the description if the first item it reveals is there.
        _item_one_false_text (str): An extension of the description if the first item it reveals is no longer there.
        _item_one_taken_status (bool): The status on if the item has been taken or not.
        _item_two_true_text (str): An extension of the description if the second item it reveals is there.
        _item_two_false_text (str): An extension of the description if the second item it reveals is no longer there.
        _item_two_taken_status (bool): The status on if the second item has been taken or not.
        _discovery_status (bool): Has the player discovered the item.
    """
    def __init__(self, initial_location: int, is_visible: bool, reveals: list[type(Item)], name: str,
                 location_text: str, description_text: str, item_one_true_text: str, item_one_false_text: str,
                 item_two_true_text: str, item_two_false_text: str):
        """
        Initialize a new dual reveals movable item.
        :param initial_location: The unique ID of the location the item spawns.
        :param is_visible: Whether the item can initially be seen or not.
        :param reveals: The item that this item reveals.
        :param name: The name of the item.
        :param location_text: A description of where the item is located.
        :param description_text: A description of the item.
        :param item_one_true_text: An extension of the description if the first item it reveals is there.
        :param item_one_false_text: An extension of the description if the first item it reveals is no longer there.
        :param item_two_true_text: An extension of the description if the second item it reveals is there.
        :param item_two_false_text: An extension of the description if the second item it reveals is no longer there.
        """
        super().__init__(initial_location, is_visible, reveals, name, location_text, description_text,
                         item_one_true_text, item_one_false_text)
        self._item_two_true_text = item_two_true_text
        self._item_two_false_text = item_two_false_text
        self._item_two_taken_status = False

    def inspect(self):
        """
        Overrides Inspect()
        Makes both items visible and therefor discovered.
        Returns a string based on if the description and if either or both of the items have been taken.
        :return: The string.
        """
        for item in self.get_revealed_item():
            item.make_visible()
        if not self.get_item_one_taken_status() and not self.get_item_two_taken_status():
            return f"{self.get_description_text()}\n{self.get_item_one_true_text()}\n{self.get_item_two_true_text()}"
        elif not self.get_item_one_taken_status() and self.get_item_two_taken_status():
            return f"{self.get_description_text()}\n{self.get_item_one_true_text()}\n{self.get_item_two_false_text()}"
        elif self.get_item_one_taken_status() and not self.get_item_two_taken_status():
            return f"{self.get_description_text()}\n{self.get_item_one_false_text()}\n{self.get_item_two_true_text()}"
        elif self.get_item_one_taken_status() and self.get_item_two_taken_status():
            return f"{self.get_description_text()}\n{self.get_item_one_false_text()}\n{self.get_item_two_false_text()}"

    def get_item_two_true_text(self):
        """
        Gets the extra text description if the item is there.
        :return: The extra description.
        """
        return self._item_two_true_text

    def get_item_two_false_text(self):
        """
        Gets the extra text description if the item is not there.
        :return: The extra description.
        """
        return self._item_two_false_text

    def get_item_two_taken_status(self):
        """
        Gets the status on if the item has been taken or not.
        :return: The status.
        """
        return self._item_two_taken_status

    def item_two_taken(self):
        """
        Sets the status to True once the item is taken.
        """
        self._item_two_taken_status = True

    def set_revealed_item(self, item):
        """
        Override as two items need to be set.
        Sets the revealed item.
        :param item: Item to be revealed.
        """
        self._reveals_item.append(item)


class RequiresInsert(Item):
    """
    This class represents an item that requires another item to be inserted for it to work.
    It inherits off item.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the item spawn.
        _is_visible (bool): Whether the item can initially be seen or not.
        _name (str): The name of the item.
        _location_text (str): A description of where the item is located.
        _description_text (str): A description of the item.
        _full_text (str): A new description for after an item has been inserted.
        _discovery_status (bool): Has the player discovered the item.
        _insert (bool): Has a item been inserted or not.
    """
    def __init__(self, initial_location: int, is_visible: bool, name: str, location_text: str, description_text: str,
                 full_text: str):
        """
        Initialize a new item.
        :param initial_location: The unique ID of the location the item spawns.
        :param is_visible: Whether the item can initially be seen or not.
        :param name: The name of the item.
        :param location_text: A description of where the item is located.
        :param description_text: A description of the item.
        :param full_text: A new description for after an item has been inserted.
        """
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._full_text = full_text
        self._insert_status = False

    def inspect(self):
        """
        Overrides Inspect()
        If the item is still empty, returns the original description, otherwise returns the full description.
        :return: The description
        """
        if not self.get_insert_status():
            return self.get_description_text()
        else:
            return self.get_full_text()

    def get_insert_status(self):
        """
        Gets the status on if the required item has been inserted or not.
        :return: The status.
        """
        return self._insert_status

    def item_inserted(self):
        """
        Sets the status to True once the required item is inserted.
        """
        self._insert_status = True

    def get_full_text(self):
        """
        Gets the description for if the item has been inserted..
        :return: The description.
        """
        return self._full_text


class Npc(Item):
    """
    This class represents a Non Player Character the adventurer can communicate with.
    It inherits off item.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the NPC spawns.
        _is_visible (bool): Whether the NPC can initially be seen or not.
        _name (str): The name of the NPC.
        _location_text (str): A description of where the NPC is located.
        _description_text (str): A description of the NPC.
        _discovery_status (bool): Has the player discovered the NPC.
    """
    def __init__(self, initial_location: int, is_visible: bool, name: str, location_text: str, description_text: str,
                 initial_text: str):
        """
        Initialize a NPC.
        :param initial_location: The unique ID of the location the NPC spawns.
        :param is_visible: Whether the NPC can initially be seen or not.
        :param name: The name of the NPC.
        :param location_text: A description of where the NPC is located.
        :param description_text: A description of the NPC.
        """
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._initial_dialogue = initial_text

    def get_initial_dialogue(self):
        """
        Gets the initial speech of the NPC.
        :return: The speech.
        """
        return self._initial_dialogue


class Dashboard(Reveals):
    """
    This class represents a specific dashboard item, that keeps track of events to complete the game.
    It inherits of reveals because it also reveals an item.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the dashboard spawns.
        _is_visible (bool): Whether the dashboard can initially be seen or not.
        _reveals_item (type(Item)): The item that this dashboard reveals.
        _name (str): The name of the dashboard.
        _location_text (str): A description of where the item is located.
        _description_text (str): A general description of the item.
        _key_false_text (str): A description when the key chamber can't be turned.
        _key_true_text (str): A description when the key chamber can be turned.
        _power_false_text (str): A description when the boat doesn't have power.
        _power_true_text (str): A description when the boat has power.
        _fuel_false_text (str): A description when fuel tank is empty.
        _fuel_true_text (str): A description when the fuel tank is full.
        _key (bool): Can the key chamber be turned.
        _power (bool): Has the boat got power.
        _fuel (bool): Has the boat got fuel.
        _discovery_status (bool): Has the player discovered the item.
    """
    def __init__(self, initial_location: int, is_visible: bool, reveals: type(Item), name: str, location_text: str,
                 description_text: str, key_false_text: str, key_true_text: str, power_false_text: str,
                 power_true_text: str, fuel_false_text: str, fuel_true_text: str):
        """
        Initialize a dashboard item.
        :param initial_location: The unique ID of the location the dashboard spawns.
        :param is_visible: Whether the dashboard can initially be seen or not.
        :param reveals: The item that this dashboard reveals.
        :param name: The name of the dashboard.
        :param location_text: A description of where the dashboard is located.
        :param description_text: A description of the dashboard.
        :param key_false_text: A description when the key chamber can't be turned.
        :param key_true_text: A description when the key chamber can be turned.
        :param power_false_text: A description when the boat doesn't have power.
        :param power_true_text: A description when the boat has power.
        :param fuel_false_text: A description when fuel tank is empty.
        :param fuel_true_text: A description when the fuel tank is full.
        """
        super().__init__(initial_location, is_visible, reveals, name, location_text, description_text)
        self._reveals_item = reveals
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
        """
        Overrides Inspect()
        Makes the reveals item visible.
        Returns a different string based on the status of the number of events completed.
        :return: The sting
        """
        self.get_revealed_item().make_visible()
        # No items
        if not self.get_key_status() and not self.get_power_status() and not self.get_fuel_status():
            return f"{self.get_key_false_text()}\n" \
                   f"{self.get_power_false_text()}\n" \
                   f"{self.get_fuel_false_text()}\n" \
                   f"{self.get_description_text()}"
        # Only key
        elif self.get_key_status() and not self.get_power_status() and not self.get_fuel_status():
            return f"{self.get_key_true_text()}\n" \
                   f"{self.get_power_false_text()}\n" \
                   f"{self.get_fuel_false_text()}\n" \
                   f"{self.get_description_text()}"
        # Only power
        elif not self.get_key_status() and self.get_power_status() and not self.get_fuel_status():
            return f"{self.get_key_false_text()}\n" \
                   f"{self.get_power_true_text()}\n" \
                   f"{self.get_fuel_false_text()}\n" \
                   f"{self.get_description_text()}"
        # Only fuel
        elif not self.get_key_status() and not self.get_power_status() and self.get_fuel_status():
            return f"{self.get_key_false_text()}\n" \
                   f"{self.get_power_false_text()}\n" \
                   f"{self.get_fuel_true_text()}\n" \
                   f"{self.get_description_text()}"
        # Key and power
        elif self.get_key_status() and self.get_power_status() and not self.get_fuel_status():
            return f"{self.get_key_true_text()}\n" \
                   f"{self.get_power_true_text()}\n" \
                   f"{self.get_fuel_false_text()}\n" \
                   f"{self.get_description_text()}"
        # Key and fuel
        elif self.get_key_status() and not self.get_power_status() and self.get_fuel_status():
            return f"{self.get_key_true_text()}\n" \
                   f"{self.get_power_false_text()}\n" \
                   f"{self.get_fuel_true_text()}\n" \
                   f"{self.get_description_text()}"
        # Power and fuel
        elif not self.get_key_status() and self.get_power_status() and self.get_fuel_status():
            return f"{self.get_key_false_text()}\n" \
                   f"{self.get_power_true_text()}\n" \
                   f"{self.get_fuel_true_text()}\n" \
                   f"{self.get_description_text()}"
        # Key, Power and Fuel
        elif self.get_key_status() and self.get_power_status() and self.get_fuel_status():
            return f"{self.get_key_true_text()}\n" \
                   f"{self.get_power_true_text()}\n" \
                   f"{self.get_fuel_true_text()}\n" \
                   f"{self.get_description_text()}"
        else:
            return "An error has occurred. Please report this to the game design team."

    def get_revealed_item(self):
        """
        Gets the item that this item reveals.
        :return: The noun.
        """
        return self._reveals_item

    def set_revealed_item(self, item):
        """
        Sets the revealed item.
        :param item: Item to be revealed.
        """
        self._reveals_item = item

    def get_key_true_text(self):
        """
        Gets the description for when the key chamber can turn.
        :return: The description.
        """
        return self._key_true_text

    def get_key_false_text(self):
        """
        Gets the description for when the key chamber can't turn.
        :return: The description.
        """
        return self._key_false_text

    def get_power_true_text(self):
        """
        Gets the description for when the boat has power.
        :return: The description.
        """
        return self._power_true_text

    def get_power_false_text(self):
        """
        Gets the description for when the boat doesn't have power.
        :return: The description.
        """
        return self._power_false_text

    def get_fuel_true_text(self):
        """
        Gets the description for when the fuel tank is full.
        :return: The description.
        """
        return self._fuel_true_text

    def get_fuel_false_text(self):
        """
        Gets the description for when the fuel tank is empty.
        :return: The description.
        """
        return self._fuel_false_text

    def get_key_status(self):
        """
        Gets the status on the key chamber turning.
        :return: The status.
        """
        return self._key

    def key_inserted(self):
        """
        Sets the key status to True.
        """
        self._key = True

    def get_power_status(self):
        """
        Gets the status on the power supply.
        :return: The status.
        """
        return self._power

    def dashboard_powered(self):
        """
        Sets the power status to True.
        """
        self._power = True

    def get_fuel_status(self):
        """
        Gets the status on the fuel tank.
        :return: The status.
        """
        return self._fuel

    def boat_fueled(self):
        """
        Sets the fuel status to True.
        """
        self._fuel = True


class FinalButton(Conditional):
    """
    This class represents a specific conditional item that can be used once the condition is met.
    It inherits off conditional.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the button spawns.
        _is_visible (bool): Whether the button can initially be seen or not.
        _name (str): The name of the button.
        _location_text (str): A description of where the button is located.
        _description_text (str): A description of the button.
        _inactive_text (str): A description before the condition is met.
        _discovery_status (bool): Has the player discovered the button.
        _condition_status (bool): Has the condition been met for another event can take place.
    """
    def __init__(self, initial_location: int, is_visible: bool, name: str, location_text: str, description_text: str,
                 inactive_text: str):
        """
        Initialize a button.
        :param initial_location: The unique ID of the location the item spawns.
        :param is_visible: Whether the item can initially be seen or not.
        :param name: The name of the item.
        :param location_text: A description of where the item is located.
        :param description_text: A description of the item.
        :param inactive_text: A description before the condition is met.
        """
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._inactive_text = inactive_text

    def get_inactive_button_text(self):
        """
        Gets the description from before the condition is met
        :return: The description.
        """
        return self._inactive_text


class Compartment(Item):
    """
    This class represents a specific compartment that requires one of two items.
    It inherits off Item
    It has the following attributes.
        _initial_location (int): The unique ID of the location the compartment spawns.
        _is_visible (bool): Whether the compartment can initially be seen or not.
        _name (str): The name of the compartment.
        _location_text (str): A description of where the compartment is located.
        _description_text (str): A description of the compartment.
        _battery_false_text (str): A description when there is no battery.
        _battery_true_text (str): A description when there is a battery.
        _power_cable_false_text (str): A description when there is no power cable.
        _power_cable_true_text (str): A description when there is a power cable.
        _discovery_status (bool): Has the player discovered the compartment.
        _battery_status (bool): Has a battery been inserted.
        _cable_status (bool): Has a power cable been inserted.
    """
    def __init__(self, initial_location: int, is_visible: bool, name: str, location_text: str,
                 description_text: str, battery_false_text: str, battery_true_text: str, power_cable_false_text: str,
                 power_cable_true_text: str):
        """
        Initialize a new compartment.
        :param initial_location: The unique ID of the location the compartment spawns.
        :param is_visible: Whether the compartment can initially be seen or not.
        :param name: The name of the compartment.
        :param location_text: A description of where the compartment is located.
        :param description_text: A description of the compartment.
        :param battery_false_text: A description when there is no battery.
        :param battery_true_text: A description when there is a battery.
        :param power_cable_false_text: A description when there is no power cable.
        :param power_cable_true_text: A description when there is a power cable.
        """
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._battery_false_text = battery_false_text
        self._battery_true_text = battery_true_text
        self._power_cable_false_text = power_cable_false_text
        self._power_cable_true_text = power_cable_true_text
        self._battery_status = False
        self._cable_status = False

    def inspect(self):
        """
        Overrides Inspect()
        Returns a different string based on the items inserted into the compartment.
        :return: The sting
        """
        if not self.get_battery_status() and not self.get_cable_status():
            return f"{self.get_description_text()}\n{self.get_battery_false_text()}\n{self.get_cable_false_text()}"
        elif not self.get_battery_status() and self.get_cable_status():
            return f"{self.get_description_text()}\n{self.get_battery_false_text()}\n{self.get_cable_true_text()}"
        elif self.get_battery_status() and not self.get_cable_status():
            return f"{self.get_description_text()}\n{self.get_battery_true_text()}\n{self.get_cable_false_text()}"
        elif self.get_battery_status() and self.get_cable_status():
            return f"{self.get_description_text()}\n{self.get_battery_true_text()}\n{self.get_cable_true_text()}"

    def get_battery_true_text(self):
        """
        Gets the description for when there is a battery inserted.
        :return: The description.
        """
        return self._battery_true_text

    def get_battery_false_text(self):
        """
        Gets the description for when there is no battery inserted.
        :return: The description.
        """
        return self._battery_false_text

    def get_cable_true_text(self):
        """
        Gets the description for when there is a cable inserted.
        :return: The description.
        """
        return self._power_cable_true_text

    def get_cable_false_text(self):
        """
        Gets the description for when there is no cable inserted.
        :return: The description.
        """
        return self._power_cable_false_text

    def get_battery_status(self):
        """
        Gets the status on the battery.
        :return: The status.
        """
        return self._battery_status

    def battery_inserted(self):
        """
        Sets the battery status to True.
        """
        self._battery_status = True

    def get_cable_status(self):
        """
        Gets the status on the power cable.
        :return: The status.
        """
        return self._cable_status

    def cable_inserted(self):
        """
        Sets the cable status to True.
        """
        self._cable_status = True


class Keypad(Item):
    """
    This class represents a specific keypad item that will unlock a container if the correct access code is entered.
    It inherits off item.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the keypad spawns.
        _is_visible (bool): Whether the keypad can initially be seen or not.
        _access_code (str): The code required to unlock the container.
        _name (str): The name of the keypad.
        _location_text (str): A description of where the keypad is located.
        _description_text (str): A description of the keypad.
        _discovery_status (bool): Has the player discovered the keypad.
    """
    def __init__(self, initial_location: int, is_visible: bool, access_code: str, name: str, location_text: str,
                 description_text: str):
        """
        Initialize a new keypad.
        :param initial_location: The unique ID of the location the keypad spawns
        :param is_visible: Whether the keypad can initially be seen or not.
        :param access_code: The code required to unlock the container.
        :param name: The name of the keypad.
        :param location_text: A description of where the keypad is located.
        :param description_text: A description of the keypad.
        """
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._access_code = access_code

    def get_access_code(self):
        """
        Gets the required access code.
        :return: The code.
        """
        return self._access_code

    def set_access_code(self, code):
        """
        Sets the required access code.
        """
        self._access_code = code


class Coconut(RevealedConsumable, Conditional):
    """
    This class represents a coconut that is revealed and can be taken once a condition is met.
    It inherits off revealed consumable and conditional.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the coconut spawns.
        _is_visible (bool): Whether the coconut can initially be seen or not.
        _energy_value: The value of energy points gained from consuming the coconut.
        _hydration_value: The value of hydration points gained from consuming the coconut.
        _revealed_by (type(Item)): The item that reveals the coconut.
        _name (str): The name of the coconut.
        _location_text (str): A description of where the coconut is located.
        _description_text (str): A description of the coconut.
        _coconut_hint_text (str): An extension of the description to help the player get it.
        _coconut_ground_text (str): A different description once it has been knocked down.
        _consumed_text (str): A description of eating the consumable.
        _discovery_status (bool): Has the player discovered the item.
        _moved_status (bool): Has the consumable been picked up by the player.
        _condition_status (bool): Has the condition been met for another event can take place.
    """
    def __init__(self, initial_location: int, is_visible: bool, energy_value: int, hydration_value: int,
                 revealed_by: type(Item), name: str, location_text: str, description_text: str, coconut_hint_text: str,
                 coconut_ground_text: str, consumed_text: str):
        """
        Initialize a new revealed consumable item.
        :param initial_location: The unique ID of the location the consumable spawns.
        :param is_visible: Whether the consumable can initially be seen or not.
        :param energy_value: The value of energy points gained from consuming the consumable.
        :param hydration_value: The value of hydration points gained from consuming the consumable.
        :param revealed_by: The noun that reveals the consumable.
        :param name: The name of the consumable.
        :param location_text: A description of where the consumable is located.
        :param description_text: A description of the consumable.
        :param coconut_hint_text: An extension of the description to help the player get it.
        :param coconut_ground_text: A different description once it has been knocked down.
        :param consumed_text: A description of eating the consumable.
        """
        super().__init__(initial_location, is_visible, energy_value, hydration_value, revealed_by, name, location_text,
                         description_text, consumed_text)
        self._coconut_hint_text = coconut_hint_text
        self._coconut_ground_text = coconut_ground_text

    def inspect(self):
        """
        Overrides Inspect()
        Gets the description depending on the status.
        :return: The description
        """
        if not self.get_condition_status():
            return f"{self.get_description_text()}\n{self.get_coconut_hint_text()}"
        else:
            return f"{self.get_description_text()}"

    def get_coconut_hint_text(self):
        """
        Gets the hint text for the coconut.
        :return: The text.
        """
        return self._coconut_hint_text

    def get_coconut_ground_text(self):
        """
        Gets the text once the coconut has been knocked down.
        :return: The text.
        """
        return self._coconut_ground_text


class WaterBottle(Consumable):
    """
    This class represents a refillable water bottle consumable item that can be consumed for  hydration.
    It inherits off consumable.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the bottle spawns.
        _is_visible (bool): Whether the bottle can initially be seen or not.
        _energy_value (int): The value of energy points gained from consuming the bottle.
        _hydration_value (int): The value of hydration points gained from consuming the bottle.
        _name (str): The name of the bottle.
        _location_text (str): A description of where the bottle is located.
        _description_text (str): A description of the bottle.
        _consumed_text (str): A description of eating the bottle.
        _empty_text (str): A description for when the bottle is empty.
        _discovery_status (bool): Has the player discovered the bottle.
        _moved_status (bool): Has the bottle been picked up by the player.
        _is_full (bool): Is the water bottle full.
    """
    def __init__(self, initial_location: int, is_visible: bool, energy_value: int, hydration_value: int, name: str,
                 location_text: str, description_text: str, consumed_text: str, empty_text: str):
        """
        Initialize a new water bottle.
        :param initial_location: The unique ID of the location the bottle spawns.
        :param is_visible: Whether the bottle can initially be seen or not.
        :param energy_value: The value of energy points gained from consuming the bottle.
        :param hydration_value: The value of hydration points gained from consuming the bottle.
        :param name: The name of the bottle.
        :param location_text: A description of where the bottle is located.
        :param description_text: A description of the bottle.
        :param consumed_text: A description of eating the bottle.
        :param empty_text: A description for when the bottle is empty.
        """
        super().__init__(initial_location, is_visible, energy_value, hydration_value, name, location_text,
                         description_text, consumed_text)
        self._empty_text = empty_text
        self._is_full = True

    def get_water_bottle_status(self):
        """
        Gets the status of the water bottle.
        :return: The status.
        """
        return self._is_full

    def fill_water_bottle(self):
        """
        Sets the water bottle status to True.
        :return: String stating water bottle filled.
        """
        self._is_full = True
        return "You fill up your water bottle."

    def empty_water_bottle(self):
        """
        Sets the water bottle status to True.
        """
        self._is_full = False


class FruitTree(RevealsMovable):
    """
    This class represents the fruit trees that reveals a multiple movable items.
    It inherits off reveals movable.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the trees spawns.
        _is_visible (bool): Whether the trees can initially be seen or not.
        _reveals_item (list[type(Item)]): The list of fruit that this trees reveals.
        _name (str): The name of the trees.
        _location_text (str): A description of where the trees are located.
        _description_text (str): A description of the trees.
        _item_one_true_text (str): An extension of the description if all the fruits it reveals are there.
        _item_one_partial_text (str): An extension of the description for if there are between 1 and 5 fruit still left.
        _item_one_false_text (str): An extension of the description if none of the fruits it reveals is are there.
        _item_one_taken (bool): The status on if the fruits has been taken or not.
        _discovery_status (bool): Has the player discovered the item.
    """
    def __init__(self, initial_location: int, is_visible: bool, reveals: list[type(Item)], name: str,
                 location_text: str, description_text: str, item_one_true_text: str, item_one_partial_text: str,
                 item_one_false_text: str):
        """
        Initialize a new fruit tree.
        :param initial_location: The unique ID of the location the trees spawns.
        :param is_visible: Whether the trees can initially be seen or not.
        :param reveals: The list of fruit that this trees reveals.
        :param name: The name of the trees.
        :param location_text: A description of where the trees are located.
        :param description_text: A description of the trees.
        :param item_one_true_text: An extension of the description if all the fruits it reveals are there.
        :param item_one_partial_text: An extension of the description for if there are between 1 and 5 fruit still left.
        :param item_one_false_text: An extension of the description if none of the fruits it reveals is are there.
        """
        super().__init__(initial_location, is_visible, reveals, name, location_text, description_text,
                         item_one_true_text, item_one_false_text)
        self._item_one_partial_text = item_one_partial_text

    def inspect(self):
        """
        Overrides Inspect()
        Creates a string with the tree description and description for each fruit not taken.
        :return: The string.
        """
        count = 0
        fruit_trees = ""
        for fruit in self.get_revealed_item():
            fruit.make_visible()
            if not fruit.get_moved_status():
                count += 1
                fruit_trees += f"{fruit.get_location_description_text()}\n"
        if count == 6:
            return f"{self.get_description_text()}\n{self.get_item_one_true_text()}\n{fruit_trees}"
        elif 0 < count < 6:
            return f"{self.get_description_text()}\n{self.get_item_one_partial_text()}\n{fruit_trees}"
        elif count == 0:
            return f"{self.get_description_text()}\n{self.get_item_one_false_text()}\n{fruit_trees}"
        else:
            return "An error has occurred. Please report this to the game design team."

    def get_item_one_partial_text(self):
        """
        Gets the description for if there are between 1 and 5 fruit still left.
        :return: The description
        """
        return self._item_one_partial_text

    def set_revealed_item(self, item):
        """
        Override as six items need to be set.
        Sets the revealed item.
        :param item: Item to be revealed.
        """
        self._reveals_item.append(item)

    def set_reveals_items_list(self, item_list):
        """
        Sets a list of fruit to reveal.
        :param item_list: Items to be revealed.
        """
        self._reveals_item = item_list


class Note(Item):
    """
    This class represents a note that is linked to another item that is neither reveals nor holds.
    It inherits off item.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the note spawns.
        _is_visible (bool): Whether the note can initially be seen or not.
        _linked (type(Item)): The item the note is linked to.
        _name (str): The name of the note.
        _location_text (str): A description of where the note is located.
        _description_text (str): A description of the note.
        _discovery_status (bool): Has the player discovered the note.
    """
    def __init__(self, initial_location: int, is_visible: bool, linked: type(Conditional), name: str,
                 location_text: str, description_text: str):
        """
        Initialize a new note.
        :param initial_location: The unique ID of the location the note spawns.
        :param is_visible: Whether the note can initially be seen or not.
        :param linked: The item the note is linked to.
        :param name: The name of the note.
        :param location_text: A description of where the note is located.
        :param description_text: A description of the note.
        """
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._linked = linked

    def inspect(self):
        """
        Overrides Inspect()
        Changes the linked items condition to be met, making it visible and returns normal description.
        :return: The description.
        """
        self.get_linked_item().condition_met()
        self.get_linked_item().get_revealed_item().condition_met()
        return f"{self.get_description_text()}"

    def get_linked_item(self):
        """
        Gets the item that note is linked to.
        :return: The revealing noun.
        """
        return self._linked


class Block(Item):
    """
    This class represents the block which 3 items can be inserted into.
    It has the following attributes.
        _initial_location (int): The unique ID of the location the block spawn.
        _is_visible (bool): Whether the block can initially be seen or not.
        _name (str): The name of the block.
        _location_text (str): A description of where the block is located.
        _description_text (str): A description of the block.
        _slot_one_item (type(Item)) or None: The block which has been inserted, or None if empty.
        _slot_two_item (type(Item)) or None: The block which has been inserted, or None if empty.
        _slot_three_item (type(Item)) or None: The block which has been inserted, or None if empty.
        _discovery_status (bool): Has the player discovered the block.
    """
    def __init__(self, initial_location: int, is_visible: bool, name: str, location_text: str,
                 description_text: str):
        """
        Initialize a new block.
        :param initial_location: The unique ID of the location the block spawn.
        :param is_visible: Whether the block can initially be seen or not.
        :param name: The name of the block.
        :param location_text: A description of where the block is located.
        :param description_text: A description of the block.
        """
        super().__init__(initial_location, is_visible, name, location_text, description_text)
        self._slot_one_item = None
        self._slot_two_item = None
        self._slot_three_item = None

    def inspect(self):
        """
        Overrides Inspect()
        Gets the description and adds to it what is in each slot.
        :return: Full description
        """
        slots = self.list_slot_items()
        description = self._description_text + "\n"
        for i, item in enumerate(slots, start=1):
            if item is None:
                description += f"Slot {i} is empty.\n"
            else:
                description += f"Slot {i} contains {item.get_name()}.\n"
        return description.strip()

    def get_slot_items(self):
        """
        Gets a description for what is in each slot.
        :return: The description.
        """
        slots = self.list_slot_items()
        description = ""
        for i, item in enumerate(slots, start=1):
            if item is None:
                description += f"Slot {i} is empty.\n"
            else:
                description += f"Slot {i} contains {item.get_name()}.\n"
        return description

    def get_slot_one_item(self):
        """
        Gets the block in slot one.
        :return: The block.
        """
        return self._slot_one_item

    def set_slot_one_item(self, item):
        """
        Sets slot one to be an item.
        :param item: The block to insert
        """
        self._slot_one_item = item

    def get_slot_two_item(self):
        """
        Gets the block in slot two.
        :return: The block.
        """
        return self._slot_two_item

    def set_slot_two_item(self, item):
        """
        Sets slot two to be an item.
        :param item: The block to insert
        """
        self._slot_two_item = item

    def get_slot_three_item(self):
        """
        Gets the block in slot three.
        :return: The block.
        """
        return self._slot_three_item

    def set_slot_three_item(self, item):
        """
        Sets slot three to be an item.
        :param item: The block to insert
        """
        self._slot_three_item = item

    def list_slot_items(self):
        """
        Creates a list with that is in each slot.
        :return: The list.
        """
        return [self.get_slot_one_item(), self.get_slot_two_item(), self.get_slot_three_item()]
