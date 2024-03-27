'''
Dictionary:  introduction,  accessing  items  in  a  dictionary  using  keys,  mutability  of  a dictionary (adding a new term, modifying an existing item), traversing a dictionary, built-in 
functions/methods – len(), dict(), keys(), values(), items(), get(), update(), del(), del,  clear(),  fromkeys(), copy(), pop(), popitem(), setdefault(), max(), min(), sorted(); Suggested programs:  count  the  number  of  times  a  character  appears  in  a  given  string  using  a dictionary, create a dictionary with names of employees, their salary and access them
'''



my_name_indict = {'fname':'raj', 'mname':'rishi', 'lname':'rana'}

print('len         : ', len(my_name_indict))
# dict() is used to typecast into dictionary
dict_keys = my_name_indict.keys()
print(dict_keys)
print(my_name_indict.values())
print(my_name_indict.items())
x = my_name_indict.get('mname')
print(x)
my_name_indict.update({'lname':'RANA', 'done':'yes'})   # will overrite if values already present or add a new key value
print(my_name_indict)
del my_name_indict['mname']
print(my_name_indict)
my_name_indict.clear()
print(my_name_indict)
questions = ['fname', 'mname','lname']
answer = 0
my_name_indict = dict.fromkeys(questions, answer)   # iterate first arg and take second arg as values
print(my_name_indict)
new_dict = my_name_indict.copy()
new_dict.pop('mname')   # delete specific key value pair
new_dict.popitem()      # delete last key value
new_dict.setdefault('fname', 'hello')   #returns the value of the item with the specified key.If the key does not exist, insert the key, with the specified value. here fname is already present therefore this statement will have no effect and will just return the value of fname
new_dict.setdefault('mname', 'rishi')
print(new_dict)
print(min(my_name_indict))
print(max(my_name_indict))
print(sorted(my_name_indict))




# count  the  number  of  times  a  character  appears  in  a  given  string  using  a dictionary, 
mystr = 'rajrishiranar'
thedict = {}
for i in mystr:
    thedict.setdefault(i, mystr.count(i))
print(thedict)
num = 0
greatest = 0
for f in thedict:
    if thedict.get(f)>num:
        num = thedict.get(f)
        greatest = f
print(greatest)



# create a dictionary with names of employees, their salary and access them
# very very ez
