class Paylips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount


    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            return self.name + " has been paid: "+ str(self.amount) + "CAD" 
        else:
            return self.name + " has not been paid yet"


diego = Paylips("Diego", "no", 1000)
maria = Paylips("Maria", "yes", 3000)
print(diego.status())
print(maria.status())

