from abc import ABC, abstractmethod

class BankAdapter(ABC):
    @abstractmethod
    def checkBalance(self) -> int:
        pass