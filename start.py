import os

user_input = ''

user_input = input("Which directory and files should we set up for you: (1)Web Basic (2)Python Script ")
parent_dir = '/Users/john/Desktop/'


print (user_input)

if user_input.isnumeric() == False:
    print("Input must be a number from the list")


if user_input == '1':
    print('Web Basic')
    directory = input("Directory Name: ")
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '% s' created" % directory)

    textFilePath = '' + '/Users/john/Desktop/' + directory + '/' + 'index.html'
    with open(textFilePath, 'w') as f:
        f.write('<!DOCTYPE html>\n<html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link rel="stylesheet" href="style.css"><script src="script.js"></script><title></title></head><body></body></html>')

    textFilePath = '' + '/Users/john/Desktop/' + directory + '/' + 'style.css'
    with open(textFilePath, 'w') as f:
        f.write('')

    textFilePath = '' + '/Users/john/Desktop/' + directory + '/' + 'script.js'
    with open(textFilePath, 'w') as f:
        f.write('')
        print ('Created Files Succesfully!')
    

if user_input == '2':
    print('Python Script')
    directory = input("Directory Name: ")
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '% s' created" % directory)

    textFilePath = '' + '/Users/john/Desktop/' + directory + '/' + 'script.py'
    with open(textFilePath, 'w') as f:
        f.write('')

    