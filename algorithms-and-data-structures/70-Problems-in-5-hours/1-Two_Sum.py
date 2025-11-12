 def twoSum(nums: List[int], target: int) -> List[int]:
     #Input: array of integer nums, integer target
     #Output: indices of two numbers that add up to the given target
     #Notes: one solution only, not use the same element twice | return the answer in any order
   
    # Using a hashmap - BigO : O(n)
    previous_map = {}
    for i in range(len(nums)):
         diff = target - nums[i]
         if diff in previous_map:
             return [previousmap[diff], i]
         previous_map[nums[i]] = i 



