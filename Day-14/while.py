'''i=1
while i<=10:
    print(i)
    i+=1'''
'''
i=10
while i>=0:
    print(i)
    i-=1'''
'''
i=2
while i<=100:
    print(i,end=' ')
    i+=2
'''
'''
s='codegnan'
i=len(s)-1
while i>=0:
    print(s[i],end='')
    i-=1
'''
''' removing zeros
l=[1,2,-1,0,2,0,3]
while 0 in l:
    l.remove(0)
print(l)'''
'''
d={}
while 1:
    product=input('p name')
    if product=='exit':
        break
    price=int(input('p price'))
    d[product]=price
print(d)
'''
i=0
while i<10:
    i+=1
    if i==15:
        break
    print(i)
else:
    print('end of loop')

