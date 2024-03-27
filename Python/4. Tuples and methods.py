'''    Tuples:  introduction,  indexing,  tuple  operations  (concatenation,  repetition,    membership and slicing);  built-in  functions/methods  –  len(),  tuple(), count(), index(), sorted(), min(), max(), sum(); tuple assignment, nested tuple; suggested programs: finding the minimum, maximum, mean of values stored in a tuple; linear search on a tuple of numbers, counting the frequency of elements in a tuple.     '''



# my_name_intuple = ('raj', 'rishi', 'rana')
# my_name_inlist = ['raj', 'rishi', 'rana']
some_nums_intuple = (1, 45, 2, 2, 5,)

# print('len        : ', len(my_name_intuple))
# print('tuple : ', tuple(my_name_inlist))

# print('count(Raj)   : ', my_name_intuple.count('Raj'))
# print('index(rishi)      : ', my_name_intuple.index('rishi'))

# print('sorted    : ', sorted(my_name_intuple))   # sorts in ascending order in form of list
# print('min    : ', min(my_name_intuple))   # 
# print('max    : ', max(my_name_intuple))
# print('sum    : ', sum(some_nums_intuple))

print('================================================')



# # finding the minimum, maximum, 
# print(min(some_nums_intuple), max(some_nums_intuple))


# # mean of values stored in a tuple; 
# print(sum(some_nums_intuple)/len(some_nums_intuple))


# linear search on a tuple of numbers, 


# counting the frequency of elements in a tuple.
count = 0
for i in some_nums_intuple:
    if i == 2:
        count += 1
print(count)





