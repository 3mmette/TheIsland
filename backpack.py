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
    """

    def __init__(self, items):
        self._backpack = []
        if items is None:
            items = []
        if type(items) != "<class 'list'>":
            items = []
        for item in items:
            self._backpack.append(item)
        self.sort()
        self.rock = False
        self.coconut = False

    def items(self):
        return self._backpack

    def sort(self):
        self._backpack.sort(key=lambda item: item.name)

    def count(self):
        if self.rock and self.coconut:
            return len(self._backpack) + 2
        elif self.rock or self.coconut:
            return len(self._backpack) + 1
        else:
            return len(self._backpack)

    def list(self):
        for item in self._backpack:
            print(f"You have a {item.name}.")
        if self.rock:
            print(f"You have a ROCK.")
        if self.coconut:
            print(f"You have a COCONUT.")
            
    def add(self, item):
        if item is not None:
            self._backpack.append(item)
            self.sort()

    def remove(self, item, current_location):
        # if an item was selected to be removed.
        if item is not None:

            # Get the index of the item using binary search.
            item_index = self.in_backpack(item)

            # If the index is greater than or equal to zero, meaning the item was found in the backpack.
            if item_index >= 0:

                # Select the item.
                selected_item = self._backpack[item_index]
                # Change its moved attribute to true.
                selected_item.moved = True
                # Add it to the list of dropped items in the current location.
                current_location.dropped_items.append(selected_item)
                # Remove the item from the backpack.
                self._backpack.remove(selected_item)
                # Resort the backpack.
                self.sort()
                print(f"{item} removed from backpack and dropped.")

            # If -1 was returned, meaning the item was not found and therefor not in the backpack.
            elif item_index < 0:
                print(f"{item} is not in your backpack.")

            # Error message if either of the others fail.
            else:
                print(f"An error occurred while searching your backpack for {item}.")

        # If no item was entered to drop.
        elif item is None:
            print(f"You did not enter an item to drop.")

        # Error message if either of the others fail.
        else:
            print(f"An error occurred. Unable to drop anything.")

    def in_backpack(self, item):
        # Get the initial range for the binary search.
        first_index = 0
        last_index = len(self._backpack) - 1

        # While the last index is bigger than the first.
        while first_index <= last_index:

            # Get the middle.
            middle_index = (first_index + last_index) // 2

            # If the middle index contains the item we are looking for
            if self._backpack[middle_index].name == item.name:
                return middle_index

            # If the item is lower than the middle index.
            elif self._backpack[middle_index].name > item.name:
                # Set the last index to the middle index minus 1, as we already searched the middle index.
                last_index = middle_index - 1

            # If the item is higher than the middle index.
            elif self._backpack[middle_index].name < item.name:
                # Set the first index to the middle index plus 1, as we already searched the middle index.
                first_index = middle_index + 1

        # If the first index is equal to or lower than the last without a result, item is not there so return index -1.
        return -1
