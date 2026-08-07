'''s='Dheeraj'
for ch in s:
    if ch in 'aeiouAEIOU':
        continue
    else:
        print(ch)
        '''
'''
l=[12,113,15,17,12,14,16,8,15]
for i in l:
    if i%2==0:
        print('even',i)
    else:
        print('odd',i)
 '''       '''
marks=(35,31,65,90)
for mark in marks:
    if mark>=35:
        print(mark,'pass')
    else:
        print(mark,'fail')
    '''
'''followers={'dheeraj','sathvik','karthik','vaibhav','vinny'}
for i in followers:
    print(i)
    #order is changed every time when executed(set unordered)
 '''   '''
bus={'s1':'booked','s2':'available','s3':'booked'}
for seat in bus:
    if bus.get(seat)=='available':
        print(seat,bus.get(seat))
        '''
#range(start,end+1,step)=>(0,nodef,1)
'''
for i in range(1,11):
    print(i)

for i in range(2,51,2):
    print(i,end=' ')

for i in range(1,100,2):
    print(i,end=' ')


'''
n=int(input('table:'))
for i in range(1,11):
    print(f'{n}*{i}={n*i}')
