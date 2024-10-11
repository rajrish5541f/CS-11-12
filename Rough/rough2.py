f1=open(r'./Rough/txt_rough0.txt', 'w+')

f1.write('hello')
f1.writelines(['maa', 'chuda'])
print(f1.read())