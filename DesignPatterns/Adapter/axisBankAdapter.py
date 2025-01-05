from bankAdapter import *
from axisBank import *

class AxisBankAdapter(BankAdapter):
    def __init__(self):
        self.bank = AxisBank()
    def checkBalance(self):
        return self.bank.bal()