import sys

a=[8,3,1,2]
n=len(a)
print(n)

def maxarray(a,n):
    res = -sys.maxsize
    for i in range(0,n):
        curr_sum=0
        for j in range(0,n):
            index=(i+j)%n
            curr_sum=curr_sum+j*a[index]

        res=max(res,curr_sum)
    return res

x=maxarray(a,n)
print("The max in the array is: ",x)
