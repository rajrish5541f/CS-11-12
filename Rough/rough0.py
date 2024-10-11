from sympy import symbols, plot

# Define the symbol and function
x = symbols('x')
expr = x**(1/2)

<<<<<<< HEAD

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


def displaywords():
    f= open(r'./Rough/txt_rough0.txt')
    while a:
        a = f.readline()
        l = a.split()
        for i in l:
            if len(i)>4:
                print(i)
displaywords()
=======
# Plot the function
plot(expr)
>>>>>>> bb607f1fa8ab42a7747a907daad9b80e0413a9a0
