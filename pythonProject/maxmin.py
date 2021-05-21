

a=[50,80,90,60,170,89,578]
def DAC_maxmin(a,i,j):
    max1=0
    max2=0
    if i==j:
        max=min=a[i]



    if i==j-1:
        if a[i]>a[j]:
            max=a[i]
            return max






        else:
            max=a[j]
            return max






    else:
        print("hi")


        mid=(i+j)/2
        (max1)=DAC_maxmin(a,i,mid)

        (max2)=DAC_maxmin(a,mid+1,j)






    if max1<max2:
        max=max2
        return max


    else:
        max=max1
        return max











i=0
j=len(a)-1
print(j)
(b)=DAC_maxmin(a,i,j)

print("The maximun element is ",b)

