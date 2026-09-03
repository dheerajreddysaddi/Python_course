from datetime import date,time,datetime,timedelta
'''today=date.today()

print(today)
print(today.day)
print(today.month)
print(today.year)
print(today.weekday())
print(n.hour)

'''
'''
n=datetime.now()
print(n)
print(n.strftime('%d-%m-%y'))
print(n.strftime('%d-%m-%Y %H:%M:%S'))
print(n.strftime('%d %d %Y %H:%M:%S %p'))
print(n.strftime('%d %B %Y %H:%M:%S %p'))
print(n.strftime('%d %d %B %Y %H:%M:%S %p'))
print(n.strftime('%A %d %B %Y %H:%M:%S %p'))'''

t=date.today()
n=datetime.now()

t7=t+timedelta(days=7)
t5=t-timedelta(days=5)

n15=n+timedelta(minutes=15)
print(t,t7,t5)
print(n,n15)