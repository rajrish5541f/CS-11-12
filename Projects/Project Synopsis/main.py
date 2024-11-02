import tkinter as tk
import mysql.connector as ml
import matplotlib.pyplot as mlt
import numpy as np
from math import *


# creating tkinter window
root = tk.Tk()
root.geometry("300x300")
root.title("Visualizer")

# setting up connection between python and MySQL
cn = ml.connect(host='localhost', user='root', passwd='1234')
curr = cn.cursor()

def start():
    """Asking user what he wants to plot: Equation or Database"""
    global what
    what = tk.StringVar()
    what.set("What do you want to plot?")
    drop = tk.OptionMenu(root, what, "Mathematical Equation", "MySQL database")
    drop.pack()

    tk.Button(root, text='Next', command=eqn_or_db).pack()

def eqn_or_db():
    # e1 is error1 which is encountered when user didn't select any option from the first drop-down menu
    e1 = tk.Label(root, text="Please select an option from the drop down menu !!!")
    if what.get()=="Mathematical Equation":
        try:
            e1.destroy()
        except: pass

        inp_eqn()
    elif what.get()=="MySQL database":
        try:
            e1.destroy()
        except: pass

        fetch_dbs()
    else:
        e1.pack()

def inp_eqn():
    """This function is meant to input Mathematical Equation."""

    # creating global variables
    global eq, eq_st, eq_end
    tk.Label(root, text='Enter equation:').pack()

    # eq is the textbox where user will enter the equation
    eq = tk.Entry(root, width=25)
    eq.pack()
    tk.Label(root, text='Define domain:').pack()

    # domain is a tkinter frame which contains 2 labels and 2 textboxes
    # where user will define the domain of the function
    domain = tk.Frame(root)
    tk.Label(domain, text='From: ').grid(row=0,column=0)
    eq_st = tk.Entry(domain, width=5)
    eq_st.grid(row=0,column=1)
    tk.Label(domain, text='To: ').grid(row=0, column=2)
    eq_end = tk.Entry(domain, width = 5)
    eq_end.grid(row=0, column=3)
    domain.pack()

    tk.Button(root, text='Plot', command=plot_eqn).pack()

def plot_eqn():
    """This function is meant to plot the equation retrieved by the inp_eqn() function."""

    # setting up variables which store the equation and domain
    eqn = eq.get()
    eqn_st = int(eq_st.get())
    eqn_end = int(eq_end.get())

    # xval is the numpy array of all the x-coordinates
    xval = np.arange((eqn_st), eqn_end, 0.1)
    x = []

    # There is possibility that the function is not defined for some values of x
    # Hence a for loop is required to separate out those x-coordinates
    # this loop will split xval array into smaller arrays which hold the x-coordinates where function is defined
    for i in xval:
        try:
            y = eval(eqn.replace('x', f"({i})"))
            x.append(i)
        except:
            mlt.plot(x,[eval(eqn.replace('x', f"({i})")) for i in x], 'b-')
            x=[]
    mlt.plot(x,[eval(eqn.replace('x', f"({i})")) for i in x],'b-', label=eqn)

    mlt.legend()
    # Finally showing up the graph
    mlt.show()

def fetch_dbs():
    """This function is meant to only fetch names of databases and return the name of chosen database"""

    # setting up global variable
    global dbname

    # executing MySQL query
    curr.execute('show databases;')

    # creating a tkinter StringVar which will hold the name of chosen database
    dbname = tk.StringVar()
    dbname.set("Select database name")

    # fetching the records
    db1 = curr.fetchall()
    dbs = []    # this will hold names of databases

    # this for loop will create the list which will hold the names of all the databases
    for i in db1:
        dbs.append(i[0])
    drop = tk.OptionMenu(root, dbname, *dbs)
    drop.pack()

    # once databases are fetched, tables will be fetched
    tk.Button(root, text='Next', command=fetch_tbs).pack()

def fetch_tbs():
    """This function is used to fetch table names"""

    # Declaring global variables
    global tbname

    # creating a tkinter StringVar which will hold the name of chosen table
    tbname = tk.StringVar()
    tbname.set('Select table name')

    # executing MySQL queries
    curr.execute('use {};'.format(dbname.get()))
    curr.execute('show tables;')
    drop = tk.OptionMenu(root, tbname, *[i[0] for i in curr.fetchall()])
    drop.pack()

    # if table names are fetched corretly then column names will be fetched
    tk.Button(root, text='Next', command=fetch_clms).pack()

def fetch_clms():
    """This function will fetch column names"""

    # declaring global variables
    global x,y,tname
    tname = tbname.get()

    # executing MySQL query
    curr.execute('describe {};'.format(tbname.get()))
    all_clms = curr.fetchall()
    desirable = ['int', 'decimal', 'numeric', 'float', 'double']

    # useable_clms is a list of only those column names which can be plotted, i.e which are numeric
    useable_clms=[]
    for i in desirable:
        for j in all_clms:
            if i in j[1]:
                useable_clms.append(j[0])

    # select_clms is a tkinter frame which allows user to choose
    # which colums to plot on x-axis and which one on y-axis
    select_clms = tk.Frame(root)
    x = tk.StringVar()
    x.set('X-axis')
    y = tk.StringVar()
    y.set('Y-axis')
    drop1 = tk.OptionMenu(select_clms, x, *useable_clms)
    drop1.grid(row=0,column=0)
    drop2 = tk.OptionMenu(select_clms, y, *useable_clms)
    drop2.grid(row=0,column=1)
    select_clms.pack()

    # Once we get column names, we will plot the graph
    tk.Button(root, text='Plot', command=plot_db).pack()

def plot_db():
    """This function is used to plot the graph of the db"""

    # declaring variables
    xaxis = x.get()
    yaxis = y.get()

    # executing query to get the records
    curr.execute('select {},{} from {} order by {}'.format(xaxis,yaxis,tname,xaxis))
    entries = curr.fetchall()
    xval, yval = [i[0] for i in entries], [i[1] for i in entries]

    # This will plot the absolute coordinates
    mlt.plot(xval, yval, marker='o', linestyle='')

    curr.execute('select {},{} from {} group by {} order by {}'.format(xaxis,f'avg({yaxis})',tname,xaxis,xaxis))
    entries = curr.fetchall()
    xval, yval = [i[0] for i in entries], [i[1] for i in entries]

    # This will plot the line of average values
    mlt.plot(xval,yval,'r--', label='Average')

    # setting x and y lables for the graph
    mlt.xlabel(xaxis)
    mlt.ylabel(yaxis)

    mlt.legend()
    # showing the graph
    mlt.show()

start()

root.mainloop()

'''
@Credits:
    ● RAJ RISHI RANA aka rajrish5541f
    ● SATYAM KUMAR
'''

