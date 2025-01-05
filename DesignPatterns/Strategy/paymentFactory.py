from creditCard import CreditCard
from debitCard import DebitCard

class PaymentFactory:
    strategies = {
        'credit_card': CreditCard,
        'debit_card': DebitCard,
    }

    @staticmethod
    def get_strategy(mode):
        available_modes = PaymentFactory.strategies.get(mode)
        if not available_modes:
            raise ValueError(f'Unknown payment mode: {mode}')
        return available_modes()