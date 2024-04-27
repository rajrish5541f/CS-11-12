l1 = [5,1,3,4,2]
n = len(l1)



for i in range(n):
    k = l1[i]
    j = i-1
    while k<l1[j] and j>=0 :
        l1[j+1] = l1[j]
        j -= 1
    else:
        l1[j+1] = k
        print('Sorted list: ', l1)