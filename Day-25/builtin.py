#import os
#os.mkdir('demo')
#os.rmdir('demo')

'''import sys
print(sys.path)
print(sys.version)
print('start')
sys.exit()
print('exit')'''

'''import platform
print(platform.system())
print(platform.release())
print(platform.processor())'''
'''
import math
print(math.pi)
print(math.e)

print(math.sqrt(36))
print(math.pow(2,3))# 2 power 3

print(math.ceil(12.00001))#upper bound ie 13
print(math.floor(12.9999))#lower bound ie 12

print(math.fabs(-10))
print(math.factorial(5))
print(math.gcd(8,24))
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(45))
print(math.degrees(30))
print(math.radians(30))'''
'''
import random

print(random.seed(10))#

print(random.randint(1,10))
print(random.randint(1000,100000))
print(random.random())#random from 0-1
print(random.uniform(1,6))#random float number

l=['R','P','S']
print(random.choice(l))
print(random.choices(l,k=2))

random.shuffle(l)
print(l)
'''

'''
from collections import Counter,defaultdict,deque
s='python programming'
m='this is that that is this is is'.split()
l=[1,1,1,1,12,3,2,3,13,43,565]
print(Counter(s))
print(Counter(l))
print(Counter(m))

d=defaultdict(int)
for i in s:
    d[i]+=1
print(d)

l=deque([])
l.append(10)
l.append(20)
l.append(30)
l.popleft()
l.popleft()
l.append(50)
l.append(70)
l.popleft()
print(l)


l=deque([])
l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(70)
l.pop()
print(l)'''


from itertools import combinations,permutations
res1=list(combinations('abc',2))
res2=list(permutations('abc',2))

print([''.join(i) for i in res1])
print([''.join(i) for i in res2])
