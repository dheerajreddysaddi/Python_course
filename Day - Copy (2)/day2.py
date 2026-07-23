Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class dog
SyntaxError: expected ':'
>>> class Dog
SyntaxError: expected ':'
>>> class  dog
SyntaxError: expected ':'
>>> 
>>> class dog:
...     print"husky"
...     
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> 
>>> class dog:
...     print'husky'
...     
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print('husky')
husky
>>> class dog:
...     print('dog')
...     print len('dog')
...     
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> class dog:
...     print('dog')
...     print (len('dog'))
... 
dog
3
