import mysql.connector as ml

cn = ml.connect(host='localhost', user='root', passwd='1234')
curr = cn.cursor()

curr.execute('show databases;')
print(curr.fetchall())

curr.execute('use sakila; show tables;')
print(curr.fetchall())

