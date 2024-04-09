#list comprehension are a way to create a new list from an already exisiting list:
# data = [1,2,3,4,5,6,7,7,8,9,10]

#the structure for creating a list comprehension: [<expression> for x in <list> <conditional>]
#add to an already exisiting list: 
# data = [x+2 for x in data]
# print('x + 2 in data list:', data)

#create a new list
# new_list = [x*2 for x in data]
# print('My new list for x*2:', new_list)

#now with if statements
# second_list = [x for x in data if x%2==0]
# print('Displaying only even numbers:', second_list)


#using range
# range_list = [x for x in range(50) if x%9==0]
# print('Nines:', range_list)


#now, for creating a dictionary given a list or multiple lists:
#{key:value, for (key,value) in <sequence> <conditional>}

#1. Using range
# my_dict_range = {x:x*2 for x in range(20)}
# print('Using range(): ',my_dict_range )

#delcaring two lists
# months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
# number = [1,2,3,4,5,6,7,8,9,10,11,12]

#Dictionary for one list:
# number_dictionary = {x:x for x in number}
# print('Dictionary of numbers:', number_dictionary)

#Dictionary with two lists:
# two_lists = {key:value for (key,value) in zip (number, months)}
# print('Two dictionary list: ', two_lists)

#now for sets, the structure of the comprehension is the same, but instead of [] we use {}
my_new_set = {x for x in range(20) if x not in [10,15,20]}
print('My new set: ', my_new_set)