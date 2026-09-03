'''try:
    #a=int(input())
    k={1:12,12:14}
    #print(k[14])
    l=[123,13]
    #print(l[2])
    #print(10/0)
    print('1'+1)
except (ValueError ,KeyError ,IndexError,ZeroDivisionError,TypeError,NameError) as e:
    print('error',e)
else:
    print("error free program")
finally:
    print('end of the program')'''

try:
    amount=int(input('enter amount:'))
    balance=5000
    if amount<0:
        raise Exception('Amount needs to be positive')
except Exception as e:
    print('error',e)
else:
    print('error free')
finally:
    print('end of program')