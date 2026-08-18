res=[i for i in range(1,11)]
print(res)

n=12
res=[i for i in range(1,n+1) if n%i==0]
print(res)

r=[12,123,32,1345,667]
res=[i if i%2==0 else 0 for i in r]
print(res)

r=[[12,23,45],[687,34,123],[34,43,90]]
res=[j for i in r for j in i if j%2==0]
print(res)

res={i for i in range(1,11)}
print(res)

n=12
res={i for i in range(1,n+1) if n%i==0}
print(res)

r=[12,123,32,1345,667]
res={i if i%2==0 else 0 for i in r}
print(res)

r=[[12,23,45],[687,34,123],[34,43,90]]
res={j for i in r for j in i if j%2==0}
print(res)

'''l=[int(input(f'Enter the number- {i+1}:'))for i in range(10)]
print(l)'''

'''name={input(f'enter names -{i+1}:'):int(input('enter marks:')) for i in range(5)}
print(name)'''

res={i:i*i for i in range(1,11)}
print(res) 