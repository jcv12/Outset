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
        f.write(f'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <link rel="stylesheet" href="style.css">\n    <script src="script.js"></script>\n    <title>{directory}</title>\n</head>\n<body>\n\n</body>\n</html>')

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

    