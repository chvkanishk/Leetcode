def maxops(nums,k):
    left= 0 
    right = len(nums)-1
    output = 0

    while left < right:
        if (nums[left] + nums[right]) == k:
            output +=1
            left+=1
            right -= 1
        elif (nums[left] + nums[right]) < k:
            left +=1
        else:
            right -=1

    return output

nums = [3,1,3,4,3]
k = 6

print(maxops(nums,k))