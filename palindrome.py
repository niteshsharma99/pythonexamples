n=int(input('Enter the number: '))
temp=n
rev=0
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)

if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

'''
n=int(input('Enter the number: '))
sum=0
while(n>0):
    r=n%10
    sum=sum+r
    n=n//10
print(sum)
'''
