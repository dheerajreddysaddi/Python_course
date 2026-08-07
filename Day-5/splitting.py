Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#int float str list tuple dict are the primary

name=int(input("Enter score")
         23
         
SyntaxError: '(' was never closed
name=int(input("Enter score"))
         
Enter score32
print(name)
         
32
value=list(map(int(input().split())))
         
21 32 32 43 23
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    value=list(map(int(input().split())))
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
value=list(map(int,input().split()))
         
32 32 12 34
print(val)
         
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(val)
NameError: name 'val' is not defined. Did you mean: 'eval'?
print(value)
         
[32, 32, 12, 34]
price= input().split
         
23 32 13 14
price
         
<built-in method split of str object at 0x000002554BE9E5B0>
price= input().split()
         
23 423 123
price
         
['23', '423', '123']
#list of strings is entered rather than am integer
         
price=list(map(int,input().split()))
         
23 12 423 1213
price
         
[23, 12, 423, 1213]
#now the list of integers is entered
         
#this can be done for the list,tuple,dict to enter array of values at same time
         
price=tuple(map(float,input().split()))
         
23.4 12 13 4
price
         
(23.4, 12.0, 13.0, 4.0)
#integer float str anything can be written (str doesn't require mapping)
         
price=set(map(float,input().split()))
         
23 21 3 34 1
price
         
{1.0, 34.0, 3.0, 21.0, 23.0}
price=dict(input().split())
         
dheeraj reddy saddi
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    price=dict(input().split())
ValueError: dictionary update sequence element #0 has length 7; 2 is required
price=dict(input().split())
         
1 2 12 3
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    price=dict(input().split())
ValueError: dictionary update sequence element #0 has length 1; 2 is required

#dict requires other operation to enter multiplt data set
         
email,pwd=input().split()
         
reddy@gmail.com reddy123
email
         
'reddy@gmail.com'
pwd
         
'reddy123'
a,b,c=input().split()
         
1 reddy 2
a
         
'1'
b
         
'reddy'
b
         
'reddy'
c
         
'2'
int(a,c)
         
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int(a,c)
TypeError: 'str' object cannot be interpreted as an integer
int(c)
         
2
int(a)
         
1
c
         
'2'
e=eval(input())
         
2 3 2 4
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    e=eval(input())
  File "<string>", line 1
    2 3 2 4
      ^
SyntaxError: invalid syntax
e=eval(input()
       1
       
SyntaxError: '(' was never closed
e=eval(input())
       
1
>>> e
...        
1
>>> e=eval(input())
...        
1.31
>>> e
...        
1.31
>>> e=eval(input())
...        
[1,2,4,5]
>>> e
...        
[1, 2, 4, 5]
>>> e=eval(input())
...        
"dheeraj"
>>> e
...        
'dheeraj'
>>> e=eval(input())
...        
('dheeraj',3,1)
>>> e
...        
('dheeraj', 3, 1)
>>> e=eval(input())
...        
{2:2,3:3,4:4}
>>> e
...        
{2: 2, 3: 3, 4: 4}
>>> e=eval(input())
...        
2*3+13/4
>>> e
...        
9.25
>>> int(e)
...        
9
>>> str(e)
...        
'9.25'
