from bankAdapter import *

class Phonepe:
    def __init__(self, Adapter: BankAdapter):
        self.Adapter = Adapter
    
    def checkBalance(self):
        return self.Adapter.checkBalance()