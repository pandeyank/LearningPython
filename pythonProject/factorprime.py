n=int(input("Enter the number:"))
 
def prime(n):

    for i in range(2,n):
        flag=True
        for j in range(2,i):
            if(i%j==0):
                flag=False
                break
    if flag==True:
        print("The prime factors is:",i)



c=prime(n)