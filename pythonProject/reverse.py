a=[]
c=0
n=int(input("Enter the number of element:"))
for i in range(0,n):
    x=int(input())
    a.append(x)
print(a)

def list_reverse(a,start,end):
    for i in a:
        if start < end:
            c=a[start]
            a[start]=a[end]
            a[end]=c
            start=start+1
            end=end-1
    print("The reverse list is:", a)
b=list_reverse(a,0,n-1)





