#Payment Gateway System
from abc import  ABC,abstractmethod
class payment(ABC):
    def pay(self):
        pass

class creditcard(payment):
    def pay(self):
        print("pay through card")
c = creditcard()
c.pay()

class upi(payment):
    def pay(self):
        print("upi")
c2 = upi()
c2.pay()
class paypal(payment):
    def pay(self):
        print("pay pal")
c3= paypal()
c3.pay()


