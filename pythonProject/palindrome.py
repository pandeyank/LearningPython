n='ABCBA'
def palindrome(n,start,end):
    for i in n:
        if n[start]==n[end]:
            start=start+1
            end=end-1
            return('Yes')
        else:
            return('No')


start=0
end=len(n)-1
x=palindrome(n,0,4)
print("The given is string is plindrome Yes or No",x)

