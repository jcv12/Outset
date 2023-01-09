import os

user_input = ''

user_input = input("Which directory and files should we set up for you: (1)Web Basic (2)Web Full Stack (3)Python Script ")

print (user_input)

if user_input == '1':
    print('Web Basic')
    directory = input("Directory Name: ")
    parent_dir = '/Users/john/Desktop/'
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '% s' created" % directory)

    f = open("index.html", "a")
    f.write("")
    f.close()

    f = open("style.css.py", "a")
    f.write("")
    f.close()

    f = open("script.js", "a")
    f.write("")
    f.close()

if user_input == '2':
    print('Script Python')
    f = open("script.py", "a")
    f.write("")
    f.close()
 
# print("File location using os.getcwd():", os.getcwd()) # Use this to find the directory you wish to use