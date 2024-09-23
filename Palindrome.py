def isPalindrome(x):
        n=x
        res=0
        if x<0:
            return False
        while n !=0:
            a=n%10
            res= res*10+a
            n=n//10
        return(res==x)

x=input("Enter a number : ")

print(isPalindrome(int(x)))