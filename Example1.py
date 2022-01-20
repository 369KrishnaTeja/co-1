class Bank:
    minbal = 10000  # it is a class attribute

    def __init__(self, acno, name, bal):
        self.name = name
        self.bal = bal
        self.acno = acno

    @classmethod
    def change_minbal(cls, amount):
        cls.minbal = amount

    # classmethods as alternative constturctors
    @classmethod
    def from_string(cls, instr):
        acno, name, bal = instr.split('-')
        return cls(acno, name, bal)

    @staticmethod
    def workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    # regular or general or instance methodds
    def details(self):
        print('Account Number: ' + self.acno)
        print('Account Holder Name: ' + self.name)
        print('Available Balance: ' + str(self.bal))
        print('Minimum Balance: ' + str(Bank.minbal))


b1 = Bank('123', 'K.Krishna Teja', 500000)
print('Instance b1....')
b1.details()

b2 = Bank.from_string('125-Ravi-500')
print('Instance creation through Classs Method')
b2.details()

Bank.change_minbal(20000)
print('Change Balance through Class Method')
print(b1.minbal)
print(b2.minbal)

import datetime

d = datetime.date(2022, 1, 1)
print('Working with static method')
if Bank.workday(d):
    print('Bank Working Day')
else:
    print('Bank Holiday')