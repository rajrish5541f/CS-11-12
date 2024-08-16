
# import csv
# fileh = open("passw.csv", 'w', newline='')
# writerh = csv.writer(fileh, delimiter=',')
# readerh = csv.reader(fileh)
# def writingPass():
#     writerh.writerow(['UserID','Password'])
#     ent = input("Welcome!\nHow many entries: ")
#     for i in range(int(ent)):
#         uid = input("Enter userID : ")
#         passw = input("Enter password : ")
#         writerh.writerow([uid, passw])
#     print("Writing entries successfull!")
#     fileh.close()


# def readingPass():
#     uID=input("Enter uID to retrieve pass : ")
#     for i in readerh:
#         if uID == i[0]:
#             print("Your password is:\n"+i[1])
#             break
#     else:
#         print("Uid not found! Try again:")
#         readingPass()
#     fileh.close()

# def changePass()
# writingPass()
# readingPass()




# from tkinter import *
# root = Tk()
# label = Label(root, text='hello world').grid(row=0, column=0)
# # label.grid()
# print(label)
# root.mainloop()


f1 = open('./Python/raj.txt', 'r')
print(type(f1.read()))