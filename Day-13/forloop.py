'''for i in range(1,11):
    print(i)          

s=input()
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        print(i,s[i])
'''
'''
l=[1,2,3,1,3,16,18]
sum=0 #type error unsupported operand if not assigned sum
for i in range(len(l)):
    if l[i]%2==0:
        sum+=l[i]
print(sum)

n=int(input())
f=1
for i in range(1,n+1):
    f=f*i
print(f)
'''
'''fibonacci
n=int(input())
a,b=0,1
for i in range(n):
    print(a,end=' ')
    a,b=b,a+b
   '''
''' dictionary of student table
d={}
n=int(input('enter no of students'))
max=0
for i in range(n):
    name=input('enter name:')
    mark=int(input('enter the marks:'))
    if mark>max:
        max=mark
    d[name]=mark
print(d)
print(f'maximum score is:{max}')
'''
'''
d={}
q=int(input('enter quantity'))
bill=0
for i in range(q):
    name=input('enter the name of product:')
    price=int(input('enter the price of product:'))
    num=int(input('number of pieces:'))
    total=price*num
    bill+=total
    d[name]=f'{price}*{num}={total}'
print(d)
print(f'total bill:{bill}')
'''

    


