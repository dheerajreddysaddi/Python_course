Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
'dheeraj' + 'reddy'
'dheerajreddy'
'dheeraj'*10
'dheerajdheerajdheerajdheerajdheerajdheerajdheerajdheerajdheerajdheeraj'
s='dheeraj'
s[4]
'r'
s[-1]
'j'
s[1]
'h'
names=['reddy dheeraj saddi']
>>> names
['reddy dheeraj saddi']
>>> names[1]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    names[1]
IndexError: list index out of range
>>> names[4]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    names[4]
IndexError: list index out of range
>>> names[:3,1]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    names[:3,1]
TypeError: list indices must be integers or slices, not tuple
>>> names=('reddy dheeraj saddi')
>>> names[:4,1]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    names[:4,1]
TypeError: string indices must be integers, not 'tuple'
>>> names='reddy dheeraj saddi'
>>> names[:6,1]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    names[:6,1]
TypeError: string indices must be integers, not 'tuple'
>>> names='reddy dheeraj saddi'
>>> names[6:11]
'dheer'
>>> names[::-1]
'iddas jareehd ydder'
>>> names[6:14]
'dheeraj '
>>> 'dheeraj '
'dheeraj '
>>> names[-1:-6:-1]
'iddas'
>>> 'dheeraj' in names
True
>>> 'reddy' mot in names
SyntaxError: invalid syntax
>>> 'reddy' not in names
False
