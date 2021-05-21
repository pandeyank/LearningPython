def gcd(m,n):
    if m==n==0:
        return 1
    if m==0:
        return n
    if n==0:
        return m
    else:
        x=(gcd(n%m,m))
        return x
p=gcd(13,23)
if p==1:
    print("Not Possible")
else:
    print("The GCD Number of the given value is:",p)