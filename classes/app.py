from classes.shop import Shop
from classes.store import Store
from classes.request import Request
from data import STORE_PRODUCTS, SHOP_PRODUCTS, STORE_CAPACITY, SHOP_CAPACITY


# ----------------------------------------------------------------
# class App to control application
class App:
    def main(self) -> None:
        """
        Logic of application
        """
        while True:
            user_request = input('Enter your request to move items: ').lower()
            phrase = Request(user_request)
            move_from, move_to = self.check_movement_params(phrase)
            if move_from.remove(phrase.product, phrase.amount):
                if move_to.add(phrase.product, phrase.amount):
                    print(f'\nКурьер забрал {phrase.amount} {phrase.product} из {phrase.from_}\n'
                          f'Курьер везет {phrase.amount} {phrase.product} из {phrase.from_}\n'
                          f'Курьер доставил {phrase.amount} {phrase.product} в {phrase.to}\n')
                    print(f"В {phrase.from_} хранится:\n"
                          f"{move_from.get_unique_items()}\n"
                          f"\nВ {phrase.to} хранится:\n"
                          f"{move_to.get_unique_items()}")
            else:
                continue
            user_answer = input("\nDo you want to move some items more? (Y/N): ").lower()
            if user_answer != "y":
                break

    def check_movement_params(self, phrase: Request):
        """
        Method to define from and to positions
        :param phrase: separated users phrase
        :return: move_from and move_to positions
        """
        store = self.create_store()
        shop = self.create_shop()
        movement_params = {
            'склад': store,
            'магазин': shop
        }
        move_from, move_to = movement_params.get(phrase.from_), movement_params.get(phrase.to)
        return move_from, move_to

    @staticmethod
    def create_store() -> Store:
        """
        static method to create a new store
        :return: Store object
        """
        store = Store(STORE_PRODUCTS, STORE_CAPACITY)
        return store

    @staticmethod
    def create_shop() -> Shop:
        """
        static method to create a new shop
        :return: Shop object
        """
        shop = Shop(SHOP_PRODUCTS, SHOP_CAPACITY)
        return shop
