'''n=int(input())
sum=0
for i in range(1,11):
    print(f'{n}*{i}={n*i}')
    sum+=n*i
print()
print(sum)'''
#print(sum(n*i for i in range (1,11)))
#print(int(input())*55)

'''n=int(input())
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)'''
#print(input()[::-1])

r1=int(input())
r2=int(input())
for i in range(r1,r2+1):
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        print(i)




