my_list = ['tamales','elotes','hot dogs']

def my_traditional(list):
    return list;

print(my_traditional(my_list))

#pure functions
my_pure = ['huevos', 'elotes']
def my_pure_function(list1, item):
    list1.copy()
    list1.append(item)
    return list1

my_new_list = my_pure_function(my_pure,3)

print(my_new_list)