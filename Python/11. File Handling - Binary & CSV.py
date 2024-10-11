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

mycsv = open(r".\Python\Resources\FH.csv", 'r+', newline='')
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
mycsvnew = open(r"./Python/Resources/FH.csv", 'a+', newline='')
writedata = csv.writer(mycsvnew, delimiter=',')
writedata.writerow(['Reyna',23,45])
mycsvnew.seek(0)
for i in csv.reader(mycsvnew, delimiter=','):
    print(i)








# write a program that copies one file to another. File names will be entered by the user.
###  open(f"{input("Enter second file's name: ")}", 'w').write(open(f"{input("Enter main file's name: ")}", 'r').read())


# write a method DISPLAYWORDS() in python to read lines from a text file  and display the words whose length is less than 4
def displaywords(x=input("Enter file name: ")):
    [print(j) for i in open(x) for j in i[0:-1].split() if len(j)>4]
displaywords()