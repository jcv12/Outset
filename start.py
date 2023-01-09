import os

user_input = ''

user_input = input("Which directory and files should we set up for you: (1)Web Basic (2)Web Full Stack (3)Python Script ")
parent_dir = '/Users/john/Desktop/'


print (user_input)

if user_input == '1':
    print('Web Basic')
    directory = input("Directory Name: ")
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '% s' created" % directory)

    textFilePath = '' + '/Users/john/Desktop/' + directory + '/' + 'index.html'
    with open(textFilePath, 'w') as f:
        f.write('')

    textFilePath = '' + '/Users/john/Desktop/' + directory + '/' + 'style.css'
    with open(textFilePath, 'w') as f:
        f.write('')

    textFilePath = '' + '/Users/john/Desktop/' + directory + '/' + 'script.js'
    with open(textFilePath, 'w') as f:
        f.write('')
        print ('Created Files Succesfully!')
    

if user_input == '2':
    print('Script Python')
    f = open("script.py", "a")
    f.write("")
    f.close()
 
# print("File location using os.getcwd():", os.getcwd()) # Use this to find the directory you wish to use