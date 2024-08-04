# Write a python function to write userIDs and passwords in a csv file and then access the password by entering the userID
import csv

def writingPass():
    fileh = open("passw.csv", 'w', newline='')
    writerh = csv.writer(fileh, delimiter=',')
    writerh.writerow(['UserID','Password'])
    ent = input("Welcome!\nHow many entries: ")
    for i in range(int(ent)):
        uid = input("Enter userID : ")
        passw = input("Enter password : ")
        writerh.writerow([uid, passw])
    print("Writing entries successfull!")
    fileh.close()




def readingPass():
    fileh = open('passw.csv', 'r')
    readerh = csv.reader(fileh)
    uID=input("Enter uID to retrieve pass : ")
    for i in readerh:
        if uID == i[0]:
            print("Your password is:\n", i[1])
            break
    else:
        print("Uid not found! Try again:")
        readingPass()
    fileh.close()


writingPass()
readingPass()
