Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s='strings.py'
>>> s.startswith('str')
True
>>> s.endswith('py')
True
>>> s.islower()
True
>>> s.isupper()
False
>>> s='Reddy'
>>> s.isupper()
False
>>> s.islower()
False
>>> 'REDDY123'.isupper()
True
>>> s.alpha()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s.alpha()
AttributeError: 'str' object has no attribute 'alpha'. Did you mean: 'isalpha'?
>>> s.isalpha()
True
>>> s.isalnum()
True
>>> print(s)
Reddy
>>> s.isnum()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
>>> 'r4@sh'.isidentifier()
False
>>> 'iredlhjdfjhdfs_'isidentifier()
SyntaxError: invalid syntax
>>> 









'iredlhjdfjhdfs_'.isidentifier()
True
