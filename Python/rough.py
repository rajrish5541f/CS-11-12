import pickle       # we'll use it to manage .dat files

fileobj = open(r".\Python\Resources\FH.dat", 'r+b')
#Inputing data
inp = ['no', 'yes', 'nope', 'yeah']

#Pickling   : storing data
if inp!='':
    pickle.dump(inp, fileobj)

#Unpickling : reading data
fileobj.seek(0)
print(pickle.load(fileobj))

fileobj.close()
# print(data)

