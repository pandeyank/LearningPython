n=int(input("Enter the number you want:"))

def prime(n):
    flag = False
    for i in range(2,n):
        if n%i==0:
            flag=True


            break
    if flag==True:
        print("The number is not Prime Number:")
    else:
        print("The number is Prime Number:")






b=prime(n)


