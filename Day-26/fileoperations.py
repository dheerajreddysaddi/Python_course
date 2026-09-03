'''file=open('pfs-63.txt','r')
print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()'''

with open('pfs-63.txt','a+')as file:
    file.write('Tom same branch ')
    file.seek(0)
    print(file.read())