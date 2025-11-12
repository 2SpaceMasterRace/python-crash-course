 def findDissappearedNumers(nums: List[int]) -> List[int]:
    #Input: array of n integers nums where nums[i] is in range of [1,n]
    #Output: array of integers in range of [1,n] that do not appear in nums

    # Just use HashSet to get that O(1) space complexity
    set_nums = set(nums)
    missing_nums = []
    
    for i in range(1, len(nums)+1):
         if i not in set_nums:
             missing_nums.append(i)
    return missing_numbers
         
    
