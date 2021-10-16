class Soda:
    def __init__(self, ingridient):
        if isinstance(ingridient, str):
            self.ingridient = ingridient
        else:
            self.ingridient = None

    def show_my_drink(self):
        if self.ingridient is None:
            print("Обычная газировка")
        else:
            print("Газировка и {}".format(self.ingridient))


if __name__ == "__main__":
    gazirovka = Soda("Малина")
    gazirovka.show_my_drink()
