list1 = ['Hello', 43, 90.08, True];

print(list1)
# now, to add an elementh, there's append the method without specify the index
list1.append(4);
print(list1, sep=" ,")


#The insert method is intented to add an element to a list at a specific position,
#specified by the index provided as an argument
list1.insert(1,'how re u')
print(list1, sep=" ,")

# to extend the list, we use the extend method
list1.extend([99,'como estas', False]);
print('Im an extended list:', list1)

# To delete
del list1[3];
print('Im  deleting the index 3:', list1)

# For each loop

for x in list1:
    print('Value', x)