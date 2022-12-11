import doctest
from typing import Union


class FoodProd:
    def __init__(self, color: str, price: Union[int, float], vegan: str) -> None:
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть str")
        self.color = color
        if not isinstance(price, (int, float)):
            raise TypeError("Калорийность должен быть типа int или float")
        if price <= 0:
            raise ValueError("Калорийность должен быть положительным числом")
        self.calories = price
        if vegan.lower() not in ('да', 'нет'):
            raise ValueError("Ответьте только 'Да' или 'Нет'")
        self.vegan = vegan  # Веганский ли продукт

    def buying(self, money_in_wallet: Union[int, float], amount: Union[int, float]) -> bool:
        """
        Фукнция проверяет, можно ли купить amount единиц товара на суммуmoney_in_wallet

        :param money_in_wallet: количество денег

        :raise TypeError: если money_in_wallet не int или float
        :raise ValueError: если money_in_wallet <= 0 (нет смысла идти в магазин без денег)

        :param amount: количество единиц товара
        int И float, так как товар может продаваться на развес

        :raise TypeError: если amount не int или float
        :raise ValueError: если amount <= 0

        :return: Удалось ли купить желаемое (True or False)

        Примеры:
        >>> product = FoodProd('Зеленый', 1, 'Да')
        >>> product.buying(1337, 5)
        """
        ...

    def discounter(self, discount) -> int:
        """
        Фукнция рассчитывает скидку на продукт, если он не веганский

        :param discount: Размер скидки в %

        :raise ValueError: если 0 > discount > 100, вызываем ошибку

        :return: Цена со скидкой, или изначальную цену(если продукт веганский)

        Примеры:
        >>> foodprod2 = FoodProd('Зеленый', 100, "Да")
        >>> foodprod2.discounter(25)
        """
        ...


class PaymentCard:
    def __init__(self, id_number: int, actual_balance: Union[int, float], currency: str) -> None:
        if not isinstance(id_number, int):
            raise TypeError("Укажите номер карты цифрами в формате int")
        if len(str(id_number)) != 16:
            raise ValueError("Укажите 16-тизначный номер карты без пробелов")
        self.id_number = id_number
        if not isinstance(actual_balance, (int, float)):
            raise TypeError("Укажите актуальный баланс в формате int или float")
        self.actual_balance = actual_balance  # может быть и нулевым, и отрицательным
        if not isinstance(currency, str):
            raise TypeError("Укажите название валюты в формате str")
        if currency.lower() not in ('dollar', 'euro', 'rulbe'):
            raise ValueError("Банк не принимает данную валюту")
        self.currency = currency

    def swift_transaction(self, incoming_currency: str, amount: Union[int, float], currency_exchange: Union[int, float]) -> int:
        """
                Функция получает перевод или снятие, расчитывает перевод в валюте карты
                и зачисляет его на баланс карты (или снимает со счета)

                :param incoming_currency: Входная валюта

                :raise ValueError: если входная валюта не входит в список используемых банком

                :param amount: Сумма перевода или снятия (отрицательная или положительная)

                :raise TypeError: если сумма указана не в (int, float)
                :raise ValueError: если сумма = 0
                :raise ValueError: если сумма снятия больше суммы на карте

                :param currency_exchange: Курс обмена двух валют.
                На мой взгляд должна быть константой от банка, а не подаваться пользователем

                :raise TypeError: если сумма указана не в (int, float)

                :return: Обновленный баланс карты

                Примеры:
                >>> swift1 = PaymentCard(1234567890123456, 500, 'euro')
                >>> swift1.swift_transaction('euro', -300, 1)
                """
        ...

    def switch_currency(self, new_currency: str, currency_exchange: Union[int, float]) -> str:
        """
                Функция меняет валюту карты и обменивает хранящиеся на ней деньги по курсу

                :param new_currency: Входная валюта

                :raise ValueError: если новая валюта не входит в список используемых банком
                :raise ValueError: если новая валюта совпадает со старой

                :param currency_exchange: Курс обмена

                :raise TypeError: если сумма указана не в (int, float)

                :return: Обновленную валюту карты
                Примеры:
                >>> first_switch = PaymentCard(1234567890123457, 501, 'euro')
                >>> first_switch.switch_currency('dollar', 60)
        """
        ...


class Solder:
    def __init__(self, name: str, rank: str, military_period: int, salary: Union[int, float]) -> None:
        if not isinstance(name, str):
            raise TypeError("Имя солдата должно быть типа str")
        self.name = name
        if not isinstance(rank, str):
            raise TypeError("Ранг солдата должен быть типа str")
        self.rank = rank
        if not isinstance(military_period, int):
            raise TypeError("Выслуга лет должна быть типа int")
        self.military_period = military_period
        if not isinstance(salary, (int, float)):
            raise TypeError("Жалование может быть только типа int и float")
        if salary < 0:  # или МРОТ
            raise TypeError("Жалование не может быть меньше 0")
        self.salary = salary

    def change_rank(self, new_rank: str, required_seniority: int) -> str:
        """
            Функция меняет ранг солдата. Понижение ранга без требований. Повышение ранга с проверкой выслуги лет

            :param new_rank: Новый ранг

            :raise TypeError: если new_rank не str
            :raise ValueError: если new_rank совпадает со старой

            :param required_seniority: Необходимая выслуга лет для повышения звания. По умолчанию 0

            :raise TypeError: если required_seniority не int
            :raise ValueError: если required_seniority < 0

            :return: новый ранг солдата
                Примеры:
                >>> solder1 = Solder("Зубенко М.П.", 'Рядовой', 3, 33333)
                >>> solder1.change_rank('Ефрейтор',1)
        """
        ...

    def changed_salary(self, salary_dif: Union[int, float]) -> Union[int, float]:
        """
            Функция меняет жалование солдата
            :param salary_dif: Изменение жалования

            :raise TypeError: если salary_dif не int или float
            :raise TypeError: если salary+salary_dif < 0

            :return: новое жалование

                Примеры:
            >>> solder1 = Solder("Жмышенко В.А.", "Полковник", 6, 50000)
            >>> solder1.changed_salary(-15000)
        """
    ...


if __name__ == "__main__":
    doctest.testmod()
    pass
