arr=[12,11,13,5,6]
def insertion_sort(arr,i):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[i+1]=arr[j]
            j=j-1
        arr[j+1]=key

i=len(arr)
p=insertion_sort(arr,i)
for i in range(len(arr)):
    print(arr[i])
