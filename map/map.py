menu = ['express','capuccino', 'chinito', 'americano', 'cortado']

def get_coffee_c(coffee):
    if coffee[0] == 'c':
        return coffee
    

# my_map_list = map(get_coffee_c, menu)
my_map_list = filter(get_coffee_c, menu)

for item in my_map_list:
    print(item)