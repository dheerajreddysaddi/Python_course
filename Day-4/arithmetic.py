Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=10
a+b
30
a/b
2.0
a-b
10
a%b
0
a*b
200
a**b
10240000000000
a**3
8000
a**2
400
a>>b
0
a<<1
40
a>b
True
a<b
False
a>>
SyntaxError: invalid syntax
a>=b
True
a<=b
False
a==b
False
a!=b
True
a+=10
a
30
a-=10
a
20
a/=4
a
5.0
a//2
2.0
a//1
5.0
a=10
b=10
a*b
100
100//10
10
100/10
10.0
n=10
m=10
n%10==0 or m%10==0
True
n%10=0
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
n%10==0 &&m%15==0
SyntaxError: invalid syntax
n%10==0 &m%15==0
True
s='dheeraj'
'e' not in s
False
'e' in s
True
l=[2,2,4,1]
5 not in l
True
5 in l
False
\
s={'dheeraj',1 ,a}
s
{1, 10, 'dheeraj'}
'd' in s
False
'd'in s
False
'dheeraj' in s
True
# list, set and dictionary are the 3 mutable data types
d={'money',:,.,'don'}
SyntaxError: invalid syntax
d={'day':4,'date':4]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
d={'day':4,'date':4}
>>> d
{'day': 4, 'date': 4}
>>> d={'day':4,'date':}
SyntaxError: expression expected after dictionary key and ':'
>>> 'day' in d
True
>>> 4 in d
False
>>> id(l)
2064231972608
>>> id(s)
2064230738720
>>> l=m
>>> l is m
True
>>> l=[1,2,3,4]
>>> m=[1,2,3,4]
>>> l is m
False
>>> id(l)
2064231972608
>>> id(m)
2064223355072
>>> l=m
>>> l is m
True
>>> l is not m
False
>>> id(l) is id(m)
False
>>> id(l)=id(m)
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
>>> id(l)==id(m)
True
>>> l!=m
False
>>> n=[1,2,3]
>>> l is n
False
>>> l=n
>>> l is n
True
>>> id(n)
2064231957184
>>> id(n)==id(l)
True
