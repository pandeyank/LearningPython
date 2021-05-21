a=[10,20,20,10,10,20,5,20,10,6,89]


def frequency(a,n):

    visited=[False for i in range(n)]

    for i in range(n):
        if visited[i]==True:
            continue
        else:
            count = 1
            for j in range(i+1,n):
                if a[i]==a[j]:
                    visited[j]=True
                    count=count+1
            print(a[i],count)

n=len(a)
print(n)
c=frequency(a,n)


