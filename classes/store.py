from classes.storage import Storage


# ----------------------------------------------------------------
# class Store, inherited from Storage base abstract class
class Store(Storage):
    def __init__(self, items: dict = None, capacity: int = 0) -> None:
        """
        Constructor method for Store
        :param items: dict with different items
        :param capacity: free space in Store
        """
        super().__init__(items, capacity)

    def add(self, name: str, quantity: int) -> bool or None:
        """
        Add an item to items dict
        :param name: name of the item
        :param quantity: count of items
        :return: True or False
        """
        if quantity > 0:
            if self.get_free_space() >= quantity:
                return super().add(name, quantity)
            else:
                print(f'No free space available. Available space in shop: {self.get_free_space()}')
        else:
            print('Quantity should be more then 0')

    def remove(self, name: str, quantity: int) -> bool:
        """
        Remove item from items dict
        :param name: name of the item
        :param quantity: count of items
        :return: True or False
        """
        if quantity > 0:
            return super().remove(name, quantity)
        else:
            print('Quantity should be more then 0')

    def get_free_space(self) -> int:
        """
        Get free space in Store
        :return: integer of free space in Store
        """
        return super().get_free_space()

    def get_items(self) -> dict:
        """
        Get all items in Store
        :return: items dict
        """
        return super().get_items

    def get_unique_items(self) -> str:
        """
        Get all unique items in Store
        :return: string of unique items in Store
        """
        return super().get_unique_items()
