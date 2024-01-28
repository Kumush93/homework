def twoSum(nums:list,target:int):
    for i in range(len(nums)):
        for k in range (i+1,len(nums)):
            if nums[i]+nums[k]==target:
                return[i,k]
print(twoSum([2,7,11,15],9))
