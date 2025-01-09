from BasePizza import BasePizza
from addons.Paneer import Paneer
from addons.cheese import Cheese

pizza = BasePizza()
paneer_pizza = Paneer(pizza)
cheese_paneer_pizza = Cheese(paneer_pizza)
print(cheese_paneer_pizza.get_price())