from os import  path


def createFile(dest):
    if not (path.isdir(dest)):
        f= open(dest, 'w')
        f.write("Welcome to Python scripting")
        f.close()


dest = r"C:\\Users\\adity\\Downloads\\python_practice\\sample.txt"


createFile(dest)

print("File created")