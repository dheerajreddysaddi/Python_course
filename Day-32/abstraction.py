from abc import ABC,abstractmethod


class Phonepe:
    def senderinfo(self):
        print('mobile number or scanner')
    def amount(self):
        print('you can enter the amount')
    def pin(self):
        print('you need to enter the pin')

    @abstractmethod
    def transaction(self):
        pass
class HDFC(Phonepe):
    def transaction(self):
        print('payment using HDFC')

class SBI(Phonepe):
    def transaction(self):
        print('payment using SBI')

class Axis(Phonepe):
    def transaction(self):
        print('payment using Axis')

class ICICI(Phonepe):
    def transaction(self):
        print('payment using ICICI')

class Union(Phonepe):
    def transaction(self):
        print('payment using Union')


dheeraj=Union()
dheeraj.senderinfo()
dheeraj.amount()
dheeraj.pin()
dheeraj.transaction()
