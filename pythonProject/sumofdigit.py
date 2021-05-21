n=67
def sumofdigit(n):
    sum = 0
    while(n!=0):
        sum=sum+(n%10)
        n=n/10
    print sum

a=sumofdigit(n)
print ["The sum of digit is", a]