import tkinter as tk
import mysql.connector as ml
import matplotlib.pyplot as mlt
import numpy as np
from math import *

from numpy.ma.extras import column_stack

root = tk.Tk()
root.geometry("300x300")
root.title("Visualizer")

cn = ml.connect(host='localhost', user='root', passwd='1234')
curr = cn.cursor()

def start():
    global what
    what = tk.StringVar()
    what.set("What do you want to plot?")
    drop = tk.OptionMenu(root, what, "Mathematical Equation", "MySQL database")
    drop.pack()

    tk.Button(root, text='Next', command=eqn_or_db).pack()

def eqn_or_db():
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
    global eq, eq_st, eq_end
    tk.Label(root, text='Enter equation:').pack()
    eq = tk.Entry(root, width=25)
    eq.pack()
    tk.Label(root, text='Define domain:').pack()
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
    eqn = eq.get()
    eqn_st = int(eq_st.get())
    eqn_end = int(eq_end.get())

    xval = np.arange((eqn_st), eqn_end, 0.1)
    x = []
    for i in xval:
        try:
            y = eval(eqn.replace('x', f"({i})"))
            x.append(i)
        except:
            mlt.plot(x,[eval(eqn.replace('x', f"({i})")) for i in x])
            x=[]
    mlt.plot(x,[eval(eqn.replace('x', f"({i})")) for i in x])

    mlt.show()

def fetch_dbs():
    global dbname
    curr.execute('show databases;')
    dbname = tk.StringVar()
    dbname.set("Select database name")
    db1 = curr.fetchall()
    dbs = []
    for i in db1:
        dbs.append(i[0])
    drop = tk.OptionMenu(root, dbname, *dbs)
    drop.pack()

    tk.Button(root, text='Next', command=fetch_tbs).pack()

def fetch_tbs():
    global tbname
    tbname = tk.StringVar()
    tbname.set('Select table name')
    curr.execute('use {};'.format(dbname.get()))
    curr.execute('show tables;')
    drop = tk.OptionMenu(root, tbname, *[i[0] for i in curr.fetchall()])
    drop.pack()

    tk.Button(root, text='Next', command=fetch_clms).pack()

def fetch_clms():
    global x,y,tname
    tname = tbname.get()
    curr.execute('describe {};'.format(tbname.get()))
    all_clms = curr.fetchall()
    desirable = ['int', 'decimal', 'numeric', 'float', 'double']
    useable_clms=[]
    for i in desirable:
        for j in all_clms:
            if i in j[1]:
                useable_clms.append(j[0])
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

    tk.Button(root, text='Plot', command=plot_db).pack()

def plot_db():
    xaxis = x.get()
    yaxis = y.get()
    curr.execute('select {},{} from {} order by {}'.format(xaxis,yaxis,tname,xaxis))
    entries = curr.fetchall()
    xval, yval = [i[0] for i in entries], [i[1] for i in entries]

    mlt.plot(xval, yval)
    mlt.xlabel(xaxis)
    mlt.ylabel(yaxis)
    mlt.show()


start()


root.mainloop()
