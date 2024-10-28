def IncreasingTriplts(nums):
    first = float('inf')
    second = float('inf')

    for i in nums:
        if i <= first:
            first = i
        elif i<= second:
            second = i
        else:
            return True
    return False

nums = [2,1,5,0,4,6]

print(IncreasingTriplts(nums))