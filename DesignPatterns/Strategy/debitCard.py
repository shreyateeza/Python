from paymentStrategy import PaymentStrategy

class DebitCard(PaymentStrategy):
    def pay(self, amount):
        print("pay with DC")