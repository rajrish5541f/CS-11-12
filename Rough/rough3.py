m,x,k=[],[],[]
a,b=input(),input()
for i in range(int(a)):
    for j in range(int(b[0])):
        x.append(input())
    m.append(x)
for i in m:
    for j in i:
        for f in j.split('.'):
            k.append(f)
    print(len(max(k)))
    k=[]
