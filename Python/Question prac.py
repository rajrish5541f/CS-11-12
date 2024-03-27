# write program to print following
'''
    *
  * * *
* * * * *
  * * *
    *

'''

import random



rnge = 5
for i in range(1, rnge+1, 2):
    print('  '*int(((rnge-i)/2))+(i*'* '))
for j in range(rnge-2, 0, -2):
    print('  '*int(((rnge-j)/2))+(j*'* '))






