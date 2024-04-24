''' Lists: introduction, indexing, list operations (concatenation, repetition, membership and 
slicing), traversing a list using loops, built-in functions/methods–len(), list(), append(), extend(), insert(), count(), index(), remove(), pop(), reverse(), sort(), sorted(), min(), max(), sum(); nested lists, suggested programs: finding the maximum, minimum, mean of numeric values stored in a list; linear search on list of numbers and counting the frequency of elements in a list '''


my_name = ['Raj', 'Rishi', 'Rana']
my_name_intuple = ('Raj', 'Rishi', 'Rana')
some_nums = [2,4,5,6, 1,2, 2, 3]
print('len        : ', len(my_name))
print('list : ', list(my_name_intuple))

my_name.append('done')
print('append(done)      : ', my_name)

my_name.extend(my_name_intuple)
print('extend      : ', my_name)    # appends all the elements of argument at last

my_name.insert(1, 'good')
print('insert(1, good)      : ', my_name)

print('count(Raj)   : ', my_name.count('Raj'))
print('index      : ', my_name.index('Rishi'))

my_name.remove('Rana')
print('remove     : ', my_name)     # will only remove the first 'Rana'

my_name.pop(1)
print('pop        : ', my_name)

my_name.reverse()
print('reverse    : ', my_name)

my_name.sort()
print('sort       : ', my_name)   # sorts in ascending order, and descending if argument is reverse=Ture

print('sorted    : ', sorted(my_name))   # sorts in ascending order
print('min    : ', min(my_name))   # 
print('max    : ', max(my_name))
print('sum    : ', sum(some_nums))

print('================================================')




# finding the maximum,

max = 0
for i in some_nums:
    if i > max :
        max = i
print(max)



# minimum, mean of numeric values stored in a list; 

print(min(some_nums))   # min val
print(sum(some_nums)/len(some_nums))    # mean val



# linear search on list of numbers and counting the frequency of elements in a list

count = 0
for i in some_nums:
    if i == 2:
        count += 1
print(count)



# search the largest word in a list
list3 = ['good', 'bad', 'sad', 'happy', 'nostalgic', 'depressed', 'motivated']
dummy = 0
largestt = []
indices = []
for i in (list3):
    if len(i) > dummy:
        dummy = len(i)
for i in range(len(list3)):
    if len(list3[i]) == dummy:
        largestt.append(list3[i])
        indices.append(i)
if len(indices) == 1:
    hverb = 'is'
    noun = 'word'
else :
    hverb = 'are'
    noun = 'words'
print(f'The largest {noun} {hverb} :')
for i in range(len(indices)):
    print(largestt[i], 'at the index', indices[i])




# w.a.p to store fibonacci series in a list
# 1 1 2 3 5 8 13
# sum of previous 2 numbers
l = [1, 1]
digi = int(input("Upto how many digits you want the series? \n  : "))
for i in range(digi - len(l)):
    l.append(l[len(l)-1] + l[len(l)-2])
print(l)