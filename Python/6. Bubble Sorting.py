'''
Suppose we have to arrange the following no.s in ascending order

2 5 3 8 4

Step 1 : Check first 2 numbers, place smaller in front and bigger in back
Step 2 : Repeat with next two no.s
Step 3... : Do this will whole list

Now the biggest number has reached the last position so dont check it

Step 4 : Do this process again upto seconds last element
.
.
.
.
.

Step 5 : Keep repeating process and reducing the last element each time.

Finally list will be sorted.

Max possible turns = No. of elements
Min                = 1

'''

# method 1
list1 = [5,3,2,6,4,1,8,7]
n = len(list1)
for i in range(n):
    for j in range(n-i-1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
print('Sorted list : ', list1)


# method 2
for i in range(n-1, 0, -1):
    for j in range(i):
        if l1[j] > l1[j+1]:
            l1[j], l1[j+1] = l1[j+1], l1[j]