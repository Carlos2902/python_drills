  #firs point, second is never part of the range, third is the step
varList = list(range(0,20,5))
print(varList)


# To iterate index over a given sequence, we can combine 
# a = ['Hola', 'Como estas', 'Bien y tu']

# for i in range(len(a)):
#     print(i, a[i])
    

#same as above but now with enumarate
# for j, v in enumerate(['a', 'b', 'c']):
#         print(j, v)

# using zip to group two or more sets
question1 = ['name?', 'zip code?'];
question2 = ['Lancelot', 'M94 0B7'];
for q, b in zip(question1, question2):
    print('Whats your {0}' 'my name is{1}'.format(q,b));