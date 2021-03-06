# Python Program to Calculate Average of Numbers
n=int(input("Enter the number of elements to be inserted: "))
a = []
for i in range(0,n):
    ele=int(input('Enter the element: '))
    a.append(ele)
avg = sum(a)/n
print(avg)
print("Average of elements in the list",round(avg,2))
