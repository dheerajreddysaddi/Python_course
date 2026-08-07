'''
username=input("username")
pwd=input("pwd")
if username=='admin' and pwd =='admin123':
    print('login succesfull')
else:
    print('invalid credentials')
    '''
'''
product=['laptop','watch','mobile']
search=input("Search Product:")
if search in product:
    print("product found")
else:
    print("product not found")
    '''
'''
bill=int(input("enter bill amount"))
if bill>99:
    print(bill)
else:
    print(bill+30)
    