class Nikita:
    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        self.name = name
        if self.name != "Никита" or self.name != "Nikita":
            self.name = "Я не {}, а Никита".format(self.name)
        self.age = age

if __name__ == "__main__":
    person1 = Nikita("Nikita", 31)
    person2 = Nikita("Иван", 14)
    print(person2.name)
    print(person1.name)
    person2.surname = "Петров"