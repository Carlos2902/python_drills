try:
    with open('ola/file.txt', 'a') as file:
        file.writelines(['\nthis is a new file using', '\n append  function']);
except FileNotFoundError as e:
    print('ERROR:', e)