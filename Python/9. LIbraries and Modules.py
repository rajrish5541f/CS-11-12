"""
Modules : To simplify programming, we create small handleable units known Modules.
A Module contains : Functions, Class & Objects, Variables, Statements, Docstrings
in-built modules are known as Standard Library Modules.

to use modules :
import math             # import whole module
import maths as m       # m is the alias name
from math import sqrt   # import just a function
from math import *      # import all functions, * means all; by this method you can directly use sqrt() and other functions instead of typing math.sqrt()

format of creating a module :
        ________________________________________
        | #modulename.py                       |
        | '''define the function'''            |    # help(modulename.py) will return this docstring
        |                                      |
        | #func1                               |
        | def func1():                         |
        |     '''tell about the function1'''   |
        |     return somevalue                 |
        |                                      |
        | #func2                               |
        | def func2():                         |
        |     '''tell about the function2'''   |
        |     return somevalue                 |
        |                                      |
        | #constants                           |
        | const1 = 3434234                     |
        |______________________________________|

--> As soon as module is imported, its main block is executed
--> If our main file also has a constant named const1 then the const1 of main file will overtake the const1 of module
--> If two modules have two functions with same name then the module imported later will overtake.







--> A collection of similar fuctions is called module.
--> A collection of modules in a single directory is called a package. __init__.py must be there in the directory.
--> A collection of many packages is called a Library. Conceptually packages and libraries are same.
"""


'''   Create a module lengthconverter.py which includes = 1.milestokm(), 2. kmtomiles(), 3. inchtofeet(), 4 feettoinch(), 5. Constants - 1 mile = 1.609344 km; 1 feet = 12 inches  '''
import lengthconverter
print(lengthconverter.milestokm(10))
help(lengthconverter)