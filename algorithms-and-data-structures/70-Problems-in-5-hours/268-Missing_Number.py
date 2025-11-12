def missingNumer(nums: List[int]) -> int:
    # Input: array of n distinct numbers in range [0,n]
    # Output: return the ONLY number that is missing from the array

    # Sorting - BigO(nlogn)
    nums.sort()
    for i in range(len(nums)+1):
        if i not in nums:
            return i
    
    # XOR - BigO(n) but space complexity is gonnna be O(1)
    xor = len(nums)
    for i in range(n):
        xor ^= i ^ nums[i]
    return xor

