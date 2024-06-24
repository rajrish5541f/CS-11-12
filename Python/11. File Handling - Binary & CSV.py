import pickle       # we'll use it to manage .dat files
                    # pickle overwrites the existing data of file

fileobj = open(r".\Python\Resources\FH.dat", 'r+b')
#Inputing data
inp = []
while True:
    a = input()
    if (a)=='':
        break
    else:
        inp.append(a)

#Pickling   : storing data
pickle.dump(inp, fileobj)

#Unpickling : reading data
fileobj.seek(0)
print(pickle.load(fileobj))

fileobj.close()

#######################################################################
import csv      # work with csv files

mycsv = open(r".\Python\Resources\FH.csv", 'r+')
readerobj = csv.reader(mycsv, delimiter=',')
for i in readerobj:
    print(i)
# another method to read csv:
mycsv.seek(0)
print(next(readerobj))
print(next(readerobj))
print(next(readerobj))
mycsv.close()

# Writing CSV
mycsvnew = open(r"./Python/Resources/FH.csv", 'a+', newline=' ')
writedata = csv.writer(mycsvnew, delimiter=',')
writedata.writerow(['Reyna',23,45])
mycsvnew.seek(0)
for i in mycsvnew:
    print(i)