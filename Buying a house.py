class Human:
    default_name = "No name"
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print("Name: {}\nAge: {}\nHouse: {}\nMoney: {}".format(self.name, self.age, self.__money, self.__house))

    @staticmethod
    def default_info():
        print("Default name: {}".format(Human.default_name))
        print("Default age: {}".format(Human.default_age))

    def earn_money(self, amount):
        self.__money += amount
        print("Earned {} money! Current value: {}".format(amount, self.__money))

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print("Not enough money")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print("Final price: {}".format(final_price))
        return final_price


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


if __name__ == "__main__":
    Human.default_info()

    alexander = Human("Sasha", 27)
    alexander.info()

    small_house = SmallHouse(8500)

    alexander.buy_house(small_house, 5)

    alexander.earn_money(5000)
    alexander.buy_house(small_house, 5)

    alexander.earn_money(20000)
    alexander.buy_house(small_house, 5)
    alexander.info()



















