from bankAdapter import *
from yesBank import *

class YesBankAdapter(BankAdapter):
    def __init__(self):
        self.bank = YesBank()

    def checkBalance(self):
        return int(self.bank.balance())