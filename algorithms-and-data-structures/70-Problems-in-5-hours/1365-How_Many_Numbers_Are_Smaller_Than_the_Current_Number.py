def smallerNumberthanCurrent(nums: List[int]) -> List[int]:
    #INPUT: array of nums 
    #OUTPUT: for each nums[i], count how many numbers are smaller than it
    #BigO: O(nlogn)
    sorted_nums = sorted(nums) 
    hashmap = {}

    for index, value in enumerate(sorted_nums): 
        if value not in hashmap:
            hashmap[nums] = index

    return_list = []

    for n in nums:
        return_list.append(hashmap[n])

    return return_list
