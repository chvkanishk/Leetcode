def ProductExceptSelf(nums):
    output= [1] * len(nums)
    left = 1
    for i in range(len(nums)):
        output[i] *= left
        left *=nums[i]

    right = 1
    for i in range(len(nums)-1,-1,-1):
        output[i] *= right
        right *= nums[i]

    return output

nums = [1,2,3,4]
print(ProductExceptSelf(nums))