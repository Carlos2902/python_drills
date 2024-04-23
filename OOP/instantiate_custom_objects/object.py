class Recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print( self.dish + " has" + str(self.items) + \
            "and it takes "+ str(self.time) + "min")
        

#instantiation
Pizza = Recipe("Pizza", ["Pechuga", "Italian Sausage", "Peperoccini"],15)
Pasta = Recipe("Pasta", ["Italian sausage", "mango"], 35)

print(Pizza.contents())
print(Pasta.contents())