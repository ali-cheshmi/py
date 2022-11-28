
a=0
b=1
n=int(input('enter num: '))
print(b,end=' ')
for i in range(1,n):
    c=a+b
    print(c,end=' ')
    if n==c:
        print('yes')
        break
    a=b
    b=c
print(i+1)