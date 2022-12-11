from abc import ABC, abstractmethod


# ----------------------------------------------------------------
# abstract base class Storage with abstractmethods and base logic
class Storage(ABC):
    @abstractmethod
    def __init__(self, items: dict = None, capacity: int = 0) -> None:
        """
        Constructor method for Storage
        :param items: dict with different items
        :param capacity: free space in Storage
        """
        self._items: dict = items
        self._capacity: int = capacity

    @abstractmethod
    def add(self, name: str, quantity: int) -> bool:
        """
        Add an item to items dict
        :param name: name of the item
        :param quantity: count of items
        :return: True or False
        """
        if name in self._items:
            self._items[name] = self._items[name] + quantity
            return True
        else:
            self._items[name] = quantity
            return True

    @abstractmethod
    def remove(self, name: str, quantity: int) -> bool:
        """
        Remove item from items dict
        :param name: name of the item
        :param quantity: count of items
        :return: True or False
        """
        if name in self._items:
            if self._items[name] < quantity:
                print(f'Такого количества {name} нет, доступно - {self._items[name]}')
                return False
            elif self._items[name] == quantity:
                self._items.pop(name)
                return True
            else:
                self._items[name] = self._items[name] - quantity
                return True
        else:
            print('Такого товара нет, выберите другой =(')
            return False

    @property
    @abstractmethod
    def get_items(self) -> dict:
        """
        Getter method to get all items
        :return: items dict
        """
        return self._items

    @abstractmethod
    def get_free_space(self) -> int:
        """
        Get free space in Storage
        :return: integer of free space in Storage
        """
        return self._capacity - sum([item for item in self._items.values()])

    @abstractmethod
    def get_unique_items(self) -> str:
        """
        Get all items in the Storage
        :return: string with definition of all items in Storage
        """
        items = '\n'.join(f"{key} в количестве {value} шт." for key, value in self._items.items())
        return items
