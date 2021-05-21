a=[20,10,2,4,7,89,45,56,72,88,75,6]
max=a[0]
max1=a[0]
for i in range(0,len(a)):
    if max<a[i]:
        max=a[i]
print('The maximum list in the array is',max)
for j in range(0,len(a)):
    if max1>a[j] and max1<max:
        max1=a[j]
print("The 2nd maximum list in the array",max1)

