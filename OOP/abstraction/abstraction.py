#abstraction methods
from abc import ABC, abstractclassmethod

class Bank(ABC):
    def basicinfo():
        return ("This is a generic bank")

    @abstractclassmethod
    def withdraw():
        pass   


class Swiss(Bank):
    def __init__(self):
        self.bal = 1000
    
    def basicinfo(self):
        return ("This is the Swiss bank")
    
    def withdraw(self, amount):
        self.amount = amount
        if amount > self.bal:
            return ("Insufficient funds")
        else:
            self.bal -= amount
            print("Amount withdrawned: "+ str(amount))
            print("New balance: " + str(self.bal))

# Driver Code
def main():
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)

if __name__ == "__main__":
    main()