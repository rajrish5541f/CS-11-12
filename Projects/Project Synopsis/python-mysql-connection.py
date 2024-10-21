import mysql.connector as sqltor
import matplotlib.pyplot as plt

db= input("Enter database name: ")

names=[
    "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah",
    "Ivan", "Jack", "Kathy", "Liam", "Mona", "Nancy", "Oscar", "Paula",
    "Quinn", "Ryan", "Sophia", "Thomas", "Uma", "Victor", "Wendy", "Xander",
    "Yara", "Zane"
]
exp=[2,2,5,7,3,2,7,4,6,9,10,3,4,2,6,34,4,7,2]
salary=[30,32,45,52,40,36,52,41,50,55,60,38,40,36,48,90,40,55,38]
credentials = {'user':'root',
               'passwd':'1234',
               'host':'localhost',
               'database': db}
cn = sqltor.connect(**credentials)
print("Connected successfully" if cn.is_connected() else "Connection to db failed")
curr = cn.cursor()

# for i in range(len(exp)):
#     curr.execute("insert into employee values ({0},'{1}',{2},{3});".format(i+1,names[i],exp[i],salary[i]))
# cn.commit()

curr.execute("select experience, avg(salary) from employee group by experience order by experience;")
data=curr.fetchall()
print(data)

xvalues=[x[0] for x in data]
yvalues=[x[1] for x in data]
# uneq=[0,]
for i in range(len(xvalues)-1):
    if xvalues[i] +1 != xvalues[i+1]:
        plt.plot([xvalues[i],xvalues[i+1]], [yvalues[i],yvalues[i+1]], "g--*", markersize=10)
    else:
        plt.plot([xvalues[i],xvalues[i+1]], [yvalues[i],yvalues[i+1]], "g-*", markersize=10)


plt.xlabel('Years of Experience')
plt.ylabel('Average salary')
plt.xticks([x for x in range(1, max(exp)+1)])
plt.show()



cn.close()