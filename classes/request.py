# class Request to control users request
class Request:
    def __init__(self, request_str: str) -> None:
        """
        Constructor method for users request
        :param request_str: users phrase from terminal input
        """
        request_str = request_str.split(' ')
        self._from = request_str[4]
        self._to = request_str[6]
        self._amount = int(request_str[1])
        self._product = request_str[2]

    @property
    def from_(self) -> str:
        """
        Getter method to get 'from' position
        :return: string with 'from' position
        """
        return self._from

    @property
    def to(self) -> str:
        """
        Getter method to get 'to' position
        :return: string with 'to' position
        """
        return self._to

    @property
    def amount(self) -> int:
        """
        Getter method to get amount
        :return: integer with 'amount' data
        """
        return self._amount

    @property
    def product(self) -> str:
        """
        Getter method to get product
        :return: string with 'product' data
        """
        return self._product
