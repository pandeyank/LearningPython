A=[20,4,8,7,6]
print("The old array list is:",A)

def rotate(A,n,d):
    for i in range(d):
        leftrotation(A,n)

def leftrotation(A,n):
    temp=A[0]
    for i in range(n):
        A[i]=A[i+1]
    A[n]=temp
    fe=A[0]
    se=A[1]
    swap(A,8,7,n)

def swap(A,fe,se,n):
    temp=fe
    for i in range(1):
        A[i]=A[i+1]
        A[i+1]=temp


def outputarray(A,n):
    print("Elements of given array is:")
    for i in range(0,len(A)):
        print(A[i])






n=len(A)-1
print(n)
x=rotate(A,n,2)
outputarray(A,n)


#outputarray(A,5)






