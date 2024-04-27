


def func(a,b):      # a,b are parameters or formal arguments/parameteres
    return a+b

print('hello')
func(2,3)           # 2,3 are arguments or actual arguments/parameters

# when this .py program is executed then the interpreter will start reading this program from 4th line, and it will read the 'func' function only when the function is called. If func is not called then interpreter won't read it

def food(sabji, roti=chapati):  # chapati is default argument
    None

food(paneer, nan)   #panner and nan are positional/required/mandatory arguments
food(dal)

# Any parameter cannot have default value unless all parameters appearing on its right have default values. example :
def interest(principal, time, rate = 0.15):pass          # correct
def interest(principal, time = 3, rate = 0.15):pass      # correct
def interest(principal, time = 2, rate):pass             # incorrect

# Named arguments example :
interest(rate = 1.2, time = 8, prin=1000)
interest(time=5, rate=0.10, prin=25000)
interest(time=5, prin=1000)
interest(1000, rate = 0.12, time=4)        # here 1000 is the positional argument and rate and time are the named arguments
# both Default argument and Named argument follow the rightmost rule, therefore the following statemnet is not valid
interest(1000, time=2, 0.15)

def sum(a,b,c):
    return a+b+c
    print("sum:", a+b+c)    # anything written after return will not get executed

# functions which return nothing are called Void Functions
# function can return multiple values, those values will be returned in for of tuple :
def sq(x,y,z):
    return x*x, y*y, z*z
t = sq(2,3,5)
t1, t2, t3 = sq(2,3,5)      # we can unpack the tuple like this


# LEGB Rule :
# L : Local
# E : Enclosing
# G : Global
# B : Built-in

# To use global variable inside local function and to avoid the creation of a seperate local variable, just write 'global' in front of it, example:
def hello():
    global x
    x = 3
    print(x)
x = 4
print(x)        # output = 4
hello()         # output = 3
print(x)        # output = 3 , bcz hello function has changed the value of x
