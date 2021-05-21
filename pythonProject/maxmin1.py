a=[50,80,90,60,170,89,578,30]
n=len(a)
print(n)
def maxmin(a,n):
    max=a[1]
    min=a[0]
    for i in range(n):
        if a[i]>max:
            max=a[i]
        if a[i]<min:
            min=a[i]
    print("The max and min element in the array list:",max,min)
x=maxmin(a,n)