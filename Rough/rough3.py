#create useable bounded stack
stack=[]
def push(x):
    stack.append(x)
def popitem():
    stack.pop()
bound=input('yes for bounded stack: ')
if bound == 'yes':
    lim = int(input('stack limit: '))
while True:
    cmd=int(input("1 for push, 2 for pop, 3 to exit: "))
    if cmd ==1:
        if bound =='no':
            push(input('enter value: '))
        elif len(stack)==lim:
            print('overflow')
        else:
            push(input('enter the value: '))
    elif cmd ==2:
        if len(stack)==0:
            print('underflow')
        else:
            popitem()
    elif cmd ==3:
        print('Code execution successful')
    else:
        print('invalid command!')
