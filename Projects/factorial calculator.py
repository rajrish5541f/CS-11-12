# Creating factorial calculator using recursion

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(int(input("Enter the number here: "))))