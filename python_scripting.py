'''import os


def current_directory():
    cwd = os.getcwd()
    print(cwd)

def file_path(filename):
    path= os.path.abspath((filename))
    print(path)

current_directory()
filename= "sample.txt"
file_path(filename)'''

'''import time

epc= time.time()
print(epc)
local_time = time.localtime(epc)
print(local_time)
print(local_time.tm_year)

print(time.ctime())'''

