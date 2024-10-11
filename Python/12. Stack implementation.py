mystack=[]

bo, length = '',0
def initialization():
    global bo, length
    bo = input('Create bounded stack?\n0. Yes\n1. No\n>>>')
    if bo == '0':
        length = input("Enter length of stack : ")
        while length.isnumeric() is False:
            length = input("Error!\nEnter a number value please : ")
        length=int(length)
    elif bo == '1':
        pass
    else:
        while bo != '0' and bo != '1':
            print('Please enter a valid argument!')
            bo = input('Create bounded stack?\n0. Yes\n1. No\n>>>')
            if bo == '0':
                length = input("Enter length of stack : ")
                while length.isnumeric() is False:
                    length = input("Error!\nEnter a number value please : ")
                length=int(length)

def push():
    if bo=='1':
        mystack.append(input('Enter the item to be pushed.\n>>>'))
        print(mystack)
    else:
        print("Overflow!") if len(mystack)==length else mystack.append(input('Enter the item to be pushed.\n>>>'))
        print(mystack)

def popitem():
    if len(mystack)!=0:
        print(mystack.pop(), 'popped successfully!')
        print(mystack)
    else:
        print('Underflow!')

initialization()
print('Stack created successfully!')
while True:
    task=input('\nWhat to do?\n1. Push\n2. Pop\n3. Show stack\n4. Exit\n>>>')
    if task=='1':
        push()
    elif task=='2':
        popitem()
    elif task=='3':
        print(mystack)
    elif task=='4':
        print("Thank You!")
        break
    else:
        print('Error! Please enter a valid argument only.')
