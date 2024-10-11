# write a function to print a string backwards using direct as well as indirect recursion

#direct method:
def reverse(x):
    if len(x)==1:
        return x
    else:
        return x[-1]+reverse(x[0:-1])
print(reverse(input("Enter the string here:  ")))

#indirect method:
def rev1(x):
    if len(x)==1:
        return x
    else:
        return x[-1]+rev2(x[0:-1])
def rev2(x):
    if len(x)==1:
        return x
    else:
        return x[-1]+rev1(x[0:-1])
print(rev1(input("Enter the string here:  ")))

