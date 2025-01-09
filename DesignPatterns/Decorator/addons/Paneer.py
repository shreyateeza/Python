from addons.pizzaAddons import PizzaAddons


class Paneer(PizzaAddons):
    def get_price(self):
        return self.pizza.get_price() + 50