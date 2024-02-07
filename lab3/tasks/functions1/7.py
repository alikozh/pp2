def has_33(nums):
    for i in range(1, len(nums)):
        if nums[i-1] == nums[i] and nums[i] == 3:
            return True
        
    return False


nums = list(map(int, input().split()))
print(has_33(nums))

