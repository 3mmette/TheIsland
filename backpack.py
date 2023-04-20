class BackPack:
    """
    BackPack Class
    ToDo: [X] Instantiate backpack
    ToDo: [X] Add Item
    ToDo: [X] Remove Item
    ToDo: [X] List Items
    ToDo: [X] Count items
    ToDo: [X] in backpack (Search for Item - Student to do)
    ToDo: [X] Sort Items

    This class represents a backpack where the adventurer can keep items.
    It has the following attributes.
        _backpack (list): Contains the items the player currently has in the backpack.
    """

    def __init__(self):
        """
        Initialize a new backpack.
        """
        self._backpack = list()

    def items(self):
        """
        Gets the list of items currently in the backpack.
        :return: The list.
        """
        return self._backpack

    def sort(self):
        """
        Sorts the backpack items into alphabetical order by their name.
        """
        self._backpack.sort(key=lambda item: item.get_name())

    def count(self):
        """
        Gets the number of items currently in the backpack.
        :return: The number of items.
        """
        return len(self._backpack)

    def list(self):
        """
        Creates a simple string for each item and adds them together.
        'You have a ____'
        :return: The string of items.
        """
        items = ""
        for item in self._backpack:
            items += f"You have a {item.get_name()}.\n"
        return items

    def add(self, item):
        """
        Adds an item and sorts the result.
        :param item: The item to add to the backpack.
        :return: A string stating the item was added.
        """
        if item is not None:
            # Add to backpack.
            self._backpack.append(item)
            # Change its moved attribute to true.
            item.item_moved()
            self.sort()
            return f"{item.get_name()} added to you bag."

    def remove(self, item, current_location):
        """
        Removes an item from the backpack if it is in there and sorts the result.
        Adds the item to the list of items in the current location.
        :param item: The item to remove from the backpack.
        :param current_location: Current location of the player.
        :return: A string stating the item was removed or not present.
        """
        # if an item was selected to be removed.
        if item is not None:

            # Get the index of the item using binary search.
            item_index = self.in_backpack(item)

            # If the index is greater than or equal to zero, meaning the item was found in the backpack.
            if item_index >= 0:

                # Select the item.
                selected_item = self._backpack[item_index]
                # Add it to the list of dropped items in the current location.
                current_location.add_item_to_location(selected_item)
                # Remove the item from the backpack.
                self._backpack.remove(selected_item)
                # Resort the backpack.
                self.sort()
                return f"{item.get_name()} removed from backpack."

            # If -1 was returned, meaning the item was not found and therefor not in the backpack.
            elif item_index < 0:
                return f"{item.get_name()} is not in your backpack."

            # Error message if either of the others fail.
            else:
                return f"An error occurred while searching your backpack for {item.get_name()}."

        # If no item was entered to drop.
        elif item is None:
            print(f"You did not enter an item to drop.")

        # Error message if either of the others fail.
        else:
            print(f"An error occurred. Unable to drop anything.")

    def in_backpack(self, item):
        """
        Competes a binary search for an item in the backpack.
        :param item: The item to search for.
        :return: The index the item is located, or -1 not present.
        """
        # Get the initial range for the binary search.
        first_index = 0
        last_index = len(self._backpack) - 1

        # While the last index is bigger than the first.
        while first_index <= last_index:

            # Get the middle.
            middle_index = (first_index + last_index) // 2

            # If the middle index contains the item we are looking for
            if self._backpack[middle_index].get_name() == item.get_name():
                return middle_index

            # If the item is lower than the middle index.
            elif self._backpack[middle_index].get_name() > item.get_name():
                # Set the last index to the middle index minus 1, as we already searched the middle index.
                last_index = middle_index - 1

            # If the item is higher than the middle index.
            elif self._backpack[middle_index].get_name() < item.get_name():
                # Set the first index to the middle index plus 1, as we already searched the middle index.
                first_index = middle_index + 1

        # If the first index is equal to or lower than the last without a result, item is not there so return index -1.
        return -1
