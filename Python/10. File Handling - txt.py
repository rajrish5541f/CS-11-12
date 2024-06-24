myfile = open(r".\Python\Resources\FH.txt", 'r+')
print(myfile.read())

###################################################################
myfile.seek(0)
print(myfile.readline())    # reads a single line; delimiter i.e. the \n at the end of the line is included
print(myfile.readline(2))
print(myfile.readline(5))

####################################################################
myfile.seek(0)
print(myfile.readlines())

#####################################################################
myfile.seek(0)
for i in myfile:
    print(i)
myfile.seek(0)
s=myfile.readline()
while s:
    print(s)
    s = myfile.readline()

#####################################################################
myfile.write('Have a good day\n')
myfile.seek(0)
print(myfile.read())

######################################################################
list1=["How're you?\n", "I'm fine.\n", "Wbu?\n"]
myfile.writelines(list1)
myfile.seek(0)
print(myfile.read())

####################################################################
import sys
myfile.seek(0)
line0=myfile.readline()
sys.stdout.write(line0)     # Will write line0 in the standard output which is monitor in this case
myinput = sys.stdin.read(1)
myfile.write(f"{myinput}\n")
sys.stderr.write("No error")





myfile.close()