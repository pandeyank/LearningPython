a=[1,2,3,5,6,7,8,9,10]
print("The older list is:",a)
n=len(a)
print(n)
d=[]

def rotate(a,n,d):
    for i in range(0,3):
        d.append(a[i])
    print("The d array list is:",d)
    print(len(d))
    x=len(d)

    j = 0
    while x<n:
        a[j]=a[x]
        j=j+1
        x=x+1
    a[n-3]=d[0]
    a[n-2]=d[1]
    a[n-1]=d[2]
    print("After the rotation list is:",a)
    w=search(a,n)
    if w==1:
        print("Number Found :")
    else:
        print("Number Not Found")

def search(a,p):
    for i in range(p):
        if a[i]==60:
            return 1

rotate(a,n,d)