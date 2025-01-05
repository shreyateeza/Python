import copy
from monster import Monster

class Sword:
    def __init__(self, val):
        self.val =val


class Zombie(Monster):
    def __init__(self, health, sword):
        self.health = health
        self.sword = sword
    
    def attack(self):
        print("Attack")
    
    def clone(self):
        return copy.deepcopy(self)