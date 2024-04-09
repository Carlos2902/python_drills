#list comprehension are a way to create a new list from an already exisiting list:
data = [1,2,3,4,5,6,7,7,8,9,10]

#the structure for creating a list comprehension: [<expression> for x in <list> <conditional>]
#add to an already exisiting list: 
data = [x+2 for x in data]
print('x + 2 in data list:', data)

#create a new list
new_list = [x*2 for x in data]
print('My new list for x*2:', new_list)

#now with if statements
second_list = [x for x in data if x%2==0]
print('Displaying only even numbers:', second_list)


#using range
range_list = [x for x in range(50) if x%9==0]
print('Nines:', range_list)