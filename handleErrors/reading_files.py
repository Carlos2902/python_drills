#for reading the whole file
# with open ('new file.txt', 'r') as file:
#     print(file.read());

#for reading characters in specific
# with open ('new file.txt', 'r') as file:
#     print(file.read(10));


#for reading the first line
# with open ('new file.txt', 'r') as file:
#     print(file.readline());

#for reading all lines and returning as a list
# with open('new file.txt', 'r') as file:
#     print(file.readlines());


# returning the whole file
with open('new file.txt', 'r') as file:
    for x in file:
        print(x) 
