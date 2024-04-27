import os 
import sample


def print_function():
    content = os.listdir(r'/Users/carlos/Documents/coursera-backend-course/modules/reload_function/')
    print('Files in this directory:')
    print(content)


print_function()
