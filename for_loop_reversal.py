n=int(input())
sum=0
while n!=0:
    sum=sum*10 + n%10
    n//=10
print(sum)