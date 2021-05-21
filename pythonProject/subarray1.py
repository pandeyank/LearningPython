a=[10,-25,130,10,80,-180,160,70]
def maxsum(a,n):
    cross_sum=0
    max_sum=0
    for i in range(n):
        max_sum=a[i]
        for j in range(i,n):
            cross_sum=cross_sum+a[j]
            if cross_sum>max_sum:
                max_sum=cross_sum
            if cross_sum<0:
                cross_sum=0
        return max_sum
n=len(a)
print(n)
x=maxsum(a,n)
print("The max subarray sum:",x)


