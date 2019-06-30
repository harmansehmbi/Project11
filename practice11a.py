class Customer:

    def __init__(self, name, membership, account):
        self.name = name
        # Dependency --> Coupling
        self.membership = membership               # HAS-A
        self.account = account                     # HAS-A

class Membership:
    pass

class Regular(Membership):
    pass

class Prime(Membership):
    pass

class BankAccount:
    pass

class SavingsAccount(BankAccount):
    pass

class CurrentAccount(BankAccount):
    pass

class LocalAccount(BankAccount):
    pass

mship = Regular()
account = SavingsAccount()


cRef = Customer("John", Regular, SavingsAccount)
