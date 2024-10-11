420, 200
x=50
def alpha(num1):
    global x
    num1+=x
    x+=20
    num1=beta(num1)
    return num1
def beta(num1):
    global x
    num1+=x
    x+=10
    num1=gama(num1)
    return num1
def gama(num1):
    global x
    x=200
    num1+=x
    return num1

num=100
num=alpha(num)
print(num,x)