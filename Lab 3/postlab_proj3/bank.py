import pickle
import random
from savingsaccount import SavingsAccount

class Bank:
    """This class represents a bank as a collection of savings accounts.
    An optional file name is also associated
    with the bank, to allow transfer of accounts to and
    from permanent file storage."""

    # The state of the bank is a dictionary of accounts and
    # a file name.  If the file name is None, a file name
    # for the bank has not yet been established.

    def __init__(self, fileName=None):
        """Creates a new dictionary to hold the accounts.
        If a file name is provided, loads the accounts from
        a file of pickled accounts."""
        self.accounts = {}
        self.fileName = fileName
        if fileName is not None:
            fileObj = open(fileName, 'rb')
            while True:
                try:
                    account = pickle.load(fileObj)
                    self.add(account)
                except EOFError:
                    fileObj.close()
                    break

    def __str__(self):
        """Returns the string representation of the bank, with accounts sorted by name."""
        accounts_sorted = sorted(self.accounts.values())
        return "\n".join(map(str, accounts_sorted))

    def makeKey(self, name, pin):
        """Returns a key for the account."""
        return name + "/" + pin

    def add(self, account):
        """Adds the account to the bank."""
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        """Removes the account from the bank and
        and returns it, or None if the account does
        not exist."""
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        """Returns the account from the bank,
        or returns None if the account does
        not exist."""
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def computeInterest(self):
        """Computes and returns the interest on
        all accounts."""
        total = 0
        for account in self.accounts.values():
            total += account.computeInterest()
        return total

    def getKeys(self):
        """Returns a sorted list of keys."""
        return sorted(self.accounts.keys())

    def save(self, fileName=None):
        """Saves pickled accounts to a file.  The parameter
        allows the user to change file names."""
        if fileName is not None:
            self.fileName = fileName
        elif self.fileName is None:
            return
        with open(self.fileName, 'wb') as fileObj:
            for account in self.accounts.values():
                pickle.dump(account, fileObj)

# Functions for testing

def createBank(numAccounts=1):
    """Returns a new bank with the given number of accounts."""
    names = ["Brandon", "Molly", "Elena", "Mark", "Tricia", "Ken", "Jill", "Jack",
         "David", "Sarah", "Bruce", "Carlos", "Eli", "Dawn", "Dylan", "Ben"]
    if numAccounts > len(names):
        raise ValueError("Number of accounts exceeds the number of unique names available")
    
    random.shuffle(names)
    selected_names = names[:numAccounts]
    
    bank = Bank()
    for i, name in enumerate(selected_names):
        balance = float(random.randint(100, 5000))
        bank.add(SavingsAccount(name, str(1000 + i), balance))
    return bank

def testAccount():
    """Test function for savings account."""
    account = SavingsAccount("Ken", "1000", 500.00)
    print(account)
    print(account.deposit(100))
    print("Expect 600:", account.getBalance())
    print(account.deposit(-50))
    print("Expect 600:", account.getBalance())
    print(account.withdraw(100))
    print("Expect 500:", account.getBalance())
    print(account.withdraw(-50))
    print("Expect 500:", account.getBalance())
    print(account.withdraw(100000))
    print("Expect 500:", account.getBalance())

def testBankSorting():
    """Creates a bank and prints its accounts to check if they are sorted by name."""
    bank = createBank(10)
    print("Accounts in the bank sorted by name:")
    print(bank)

def main(number=8, fileName=None):
    """Creates and prints a bank, either from the optional file name argument or from the optional number."""
    testBankSorting()

if __name__ == "__main__":
    main()