def flowers(flowerbed,n):
    l = len(flowerbed)
    i=0
    while i <l and n>0:
        if flowerbed[i] == 1:
            i+=2
        elif i ==l-1 or flowerbed[i+1] == 0:
            n-=1
            i+=2
        else:
            i+=3
    return n<=0

flowerbed = [1,0,0,0,1]
n = 2
print(flowers(flowerbed,n))