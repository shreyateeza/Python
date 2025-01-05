import copy

class place:
    def __init__(self, street):
        self.street = street


class attendance:
    def __init__(self, value):
        self.value = value


class Person:
    def __init__(self, name, age, adr, attd):
        self.name = name
        self.age = age
        self.place = adr
        self.att = attd

    def __copy__(self):
        new_att = copy.deepcopy(self.att)
        return Person(self.name, self.age, self.place, new_att)


person = Person("abc", 25, place("abc"))
person4 = person

# Shallow Copy
person2 = copy.copy(person)
person3 = copy.deepcopy(person)
print(person3)
person5 = person.__copy__()
