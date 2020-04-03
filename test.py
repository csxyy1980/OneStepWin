# -*- coding:utf-8 -*-
# to make .exe by using command: pyinstaller --console --onefile test.py


import  numpy
print(numpy.__version__)

print("hello wolrd")
list = [1,2,3,4,5]
for i in list:
    print(i)

tuple = (1,2,3,4,5)
for i,k in enumerate(tuple):
    print(i,":",k)
