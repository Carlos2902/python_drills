import random

f_name = input('Enter file name: ')
f_read_file = open(f_name) #r is default, so not need to explicitly write it
#now, read the whole file
f_content_display = f_read_file.read();
#now, put it all into a list
f_list = f_content_display.split('\n')

f_read_file.close()
print(random.choice(f_list))