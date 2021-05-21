a=[]
x=int(input("Enter the number of elements in an array:"))
for i in range(0,x):
    ele=int(input())
    a.append(ele)
print(len(a))

def arraysum(a,start,end):
    sum=0
    for i in a:
        sum=sum+i
    return(sum)
start=0;
end=len(a)-1
b=arraysum(a,0,end)
print("The sum of the array:",b)
