#Class names are capitalized and use camelCase
# Self must be specified with the __init__ or __new__ default constructor for the class is being created
# Classes being created are what is known as encapsulation
import datetime
import pytz


class Account:
    """ Simple account class with balance """
    # Theres a warning when not using self in this method that can be a static method that is shared amongst all instances
    # Removing the self and adding the @staticmethod before the method creates a static non mutable method
    # Also remember that a non public method's definition starts with underscore _currentTime()
    @staticmethod
    def _currenttime():
        utc_Time = datetime.datetime.now()
        return pytz.utc.localize(utc_Time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transActions = []
        if balance > 0:
            self._transActions.append((Account._currenttime(), balance))

        # Or adding the initial balance to the transactions list could be done with
        # self.transactions = [(Account.currenttime(), balance)
        print("Account created for " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.showbalance()
            # The current time can then be used to append the transaction list
            # self.transActions.append((pytz.utc.localize(datetime.datetime.now()), amount))
            # Self._currentTime() is also ok, but there' a slight performance drag
            self._transActions.append((Account._currenttime(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.showbalance()
            self._transActions.append((Account._currenttime(), -amount))
        else:
            print("Must be greater than zero and less than account balance")

    def showbalance(self):
        print("Balance is {}".format(self.__balance))

    def showtransactions(self):
        # Remember that the transactions is stored as a tuple and unpacking a tuple you can assign multiple values
        for date, amount in self._transActions:
            if amount > 0:
                transType = "deposited"
            else:
                transType = " withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {}".format(amount, transType, date, date.astimezone()))


if __name__ == '__main__':
    dustin = Account('Dustin', 10000)
    dustin.deposit(1000)
    dustin.showtransactions()
    dustin.withdraw(5000)

    jonni = Account('Jonni', 800)
    jonni.deposit(100)
    jonni.withdraw(200)
    jonni.showtransactions()
    # The issue with not making the class methods "private" although they still can be changed is that in the
    # case below we can modify the balance without it showing on the transaction list. A better way is to use
    # either the single underscore for class methods _ or the __ which then hides the method from being changed
    # The double underscore isn't really all that practical because you can still change the items if you
    # do jonni._Account__balance = 200 this is known as *MANGLING in python
    jonni.__balance = 200
    jonni.showbalance()