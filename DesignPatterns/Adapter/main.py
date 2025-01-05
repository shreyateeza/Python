from yesBankAdapter import *
from axisBankAdapter import *
from phonepe import Phonepe

if __name__ == '__main__':
    b = AxisBankAdapter()
    p = Phonepe(b)
    print((p.checkBalance()))