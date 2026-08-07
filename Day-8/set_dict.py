Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s={}
type(s)
<class 'dict'>
s=set()
s={1,2,3,4,14,17,8132}
s
{1, 2, 3, 8132, 4, 17, 14}
s=set()
s
set()
s.add(1)
s.add(12.3)
s.add(2+4j)
s
{1, 12.3, (2+4j)}
s={1,1,1,1,1,1}
s
{1}
l={10,20,30}
m={1,2,3,4}
l+m
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    l+m
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a={1,2,3,4,5}]
SyntaxError: unmatched ']'
a={1,2,3,4,5}
b={7,8,0,12}
a|b
{0, 1, 2, 3, 4, 5, 7, 8, 12}
a&b
set()
a={1,3,5,2}
b={2,5,1}
a&b
{1, 2, 5}
a-b
{3}
a^b
{3}
{1}<=a
True
{1,2,3,5}<=a
True
{1,2,4,5}<=a
False
a>={1}
True
a>={1,2,4,5}
False
a<={1,2,4,5}
False
a<=b
False
a={1,2,4,2}
b={1,4,2}
a<=b
True
a.isdisjoint(b)
False
a.isdisjoint({1,2})
False
a.issubset(b)
True
a.union(b)
{1, 2, 4}
a.intersection(b)
{1, 2, 4}
a={1,2,3,4,5}
b={9,3,5,7}
a.intersection(b)
{3, 5}
a.union(b)
{1, 2, 3, 4, 5, 7, 9}
a.issubset(b)
False
a.issuperset(b)
False
max(a)
5
min(a)
1
sorted(a)
[1, 2, 3, 4, 5]
sum(a)
15
a
{1, 2, 3, 4, 5}
b=a
b
{1, 2, 3, 4, 5}
b.add(6)
b
{1, 2, 3, 4, 5, 6}
a
{1, 2, 3, 4, 5, 6}
c=a.copy()
c.add(7)
c
{1, 2, 3, 4, 5, 6, 7}
a
{1, 2, 3, 4, 5, 6}
#using copy function we can only change the copied value other than real value
a
{1, 2, 3, 4, 5, 6}
a.pop()
1
a.pop()
2
a
{3, 4, 5, 6}
a.update(1,2)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a.update(1,2)
TypeError: 'int' object is not iterable
a.update({1,2})
a
{1, 3, 4, 5, 6, 2}
#update does not follow the order
a.remove(4)
a
{1, 3, 5, 6, 2}
a.remove(4)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a.remove(4)
KeyError: 4
a.discard(4)
#discard handles the keyerror even if it is not present the the set
len(a)
5
all(a)
True
any(a)
True
a=frozenset({1,12,311,21,4})
a
frozenset({1, 4, 21, 311, 12})
a.add(12)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    a.add(12)
AttributeError: 'frozenset' object has no attribute 'add'
d={}
d=dict()
type(d)
<class 'dict'>
d={}
type(d)
<class 'dict'>
d={'k1':'n1','k2':'n2'}
d
{'k1': 'n1', 'k2': 'n2'}
id(d)
2259372027008
d['k3']=['v3']
d
{'k1': 'n1', 'k2': 'n2', 'k3': ['v3']}
d['k3']='v3'
d
{'k1': 'n1', 'k2': 'n2', 'k3': 'v3'}
d={}
d[1]='int'

d
{1: 'int'}
d[1]=21
d[12.3]='float
SyntaxError: unterminated string literal (detected at line 1)
d[12.3]='float'
d
{1: 21, 12.3: 'float'}
d['str']=str
>>> d
{1: 21, 12.3: 'float', 'str': <class 'str'>}
>>> d[(1,2,3,4)]='tuple'
>>> d
{1: 21, 12.3: 'float', 'str': <class 'str'>, (1, 2, 3, 4): 'tuple'}
>>> d[[1,2,3,3]]='list'
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    d[[1,2,3,3]]='list'
TypeError: unhashable type: 'list'
>>> d[(1,2,3)]='SET'
>>> d
{1: 21, 12.3: 'float', 'str': <class 'str'>, (1, 2, 3, 4): 'tuple', (1, 2, 3): 'SET'}
>>> d[{1,2,3}]='set'
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    d[{1,2,3}]='set'
TypeError: unhashable type: 'set'
>>> d[1:2]='dict'
>>> d
{1: 21, 12.3: 'float', 'str': <class 'str'>, (1, 2, 3, 4): 'tuple', (1, 2, 3): 'SET', slice(1, 2, None): 'dict'}
>>> 12.3 in d
True
>>> 'str' in d
True
>>> 'tuple' in d
False
>>> #because keys are accesed not values
>>> d[1]
21
>>> d[12.3]
'float'
>>> d['str']
<class 'str'>
>>> d[4]
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    d[4]
KeyError: 4
>>> d.get(4)
>>> d.get(4,'not present in dictionary')
'not present in dictionary'
>>> d.get(1,'not present')
21
>>> #get handles the keyerrors
