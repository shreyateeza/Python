from paymentStrategy import PaymentStrategy

class CreditCard(PaymentStrategy):
    def pay(self, amount):
        print("paid using CC")