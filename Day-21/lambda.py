'''greater= lambda a,b: a if a>b else b
print(greater(11,14))
print(greater(15,14))
print(greater(11,21))

wish= lambda name:f'welcome{name}'
print(wish(' Dheeraj'))
print(wish(' sathvik'))

iseven=lambda a:'even' if a%2==0 else 'odd'
print(iseven(23))
print(iseven(22))

avg= lambda a,b,c:(a+b+c)/3
print(avg(12,32,14))
print(avg(12,33,56))

domain= lambda mail:(mail.split('@')[-1]).split('.')[0]
print(domain('dheerajsaddi@gmail.com'))
print(domain('dheerajsaddi@yahoo.com'))

gst=lambda p:p+p*0.18
print(gst(10000))
print(gst(3000))

prices=[5678,1234,56,1232]
res=list(map(lambda p:p+p*0.18,prices))
print(res)

names=['dheeraj','sathvik','spandana','prabhas']
res=list(map(lambda name:name.title(),names))
print(res)

prices=[5678,1234,56,1232]
res=list(map(lambda p:p-p*0.3,prices))
print(res)

prices=[5635,3213,4312,6645]
res=list(filter(lambda price:price%2!=0,prices))
print(res)

names=['dheeraj','sathvik','spandana','prabhas']
res=list(filter(lambda name:len(name)>7,names))
print(res)

from functools import reduce
l=[3,5,45,12,343]
res= reduce(lambda sum,i:sum+i,l)
print(res)

names=['dheeraj','sathvik','spandana','prabhas']
res=reduce(lambda res,i:res+' '+i,names)
print(res)
'''

products={'sugar':50,
          'salt':20,
          'milk':30,
          'bread':40}
print(dict(sorted(products.items())))
print(dict(sorted(products.items(),reverse=True)))

print(dict(sorted(products.items(),key=lambda i:i[1])))
print(dict(sorted(products.items(),key=lambda i:i[1],reverse=True)))