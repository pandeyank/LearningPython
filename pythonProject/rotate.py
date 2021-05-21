a=[1,2,3,4,5,]
print("The oldest array is:",a)
n=len(a)
x=n-1
print(x)
def rotate(a,x):
    temp=a[x]
    for i in range(x,0,-1):
        a[i]=a[i-1]
    a[0]=temp
    for i in range(x+1):
        print("The new array list is:",a[i])









rotate(a,x)
