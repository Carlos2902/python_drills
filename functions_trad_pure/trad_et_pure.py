listNumber = [1,2,3]

#traditional functions can manipulate the global scope
def add_to_list(item):
    return listNumber.append(item);

add_to_list(3)
#print the list wey!! no la funcion jaja
print(listNumber)

#PURE functions don't alterate the global scope, which makes them easy to debug
my_list = [2,3,4]
def my_pure_function(list1,item):
    list1.copy()
    list1.append(item)
    return list1

my_new_list = my_pure_function(my_list,5)

print(my_new_list)