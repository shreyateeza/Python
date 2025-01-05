from androidFactory import AndroidFactory
from iosFactory import IosFactory

class OSFactory:
    def decide(self, val):
        if val == "Android":
            return AndroidFactory()
        else:
            return IosFactory()