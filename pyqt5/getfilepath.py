import os
a = open('getfilepath.py')
b = os.path.realpath(a.name)
print(b)