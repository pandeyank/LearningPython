a=[20,-25,130,-80,10,90,-43,12,-40]


def subarraysum(a,n):
    max_sum = 0
    cross_sum = 0
    for i in range(n):
        cross_sum=cross_sum+a[i]
        if cross_sum>max_sum:
            max_sum=cross_sum
        if cross_sum<0:
            cross_sum=0

    return(max_sum)
n=len(a)
print(n)
x=subarraysum(a,n)
print("The max sub array sum is:",x)