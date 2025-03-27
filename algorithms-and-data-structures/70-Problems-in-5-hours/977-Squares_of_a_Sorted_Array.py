def sortedSquares(nums: List[int]) -> List[int]:
    # INPUT: array of nums sorted in a non-decreasing order
    # OUTPUT: return an array of squares

    # Brute Force - BigO(nlogn)
    squared_list = [num**2 for num in nums]
    return squared_list.sort()

    # Optimized solution using two pointers
    squared_list = collections.deque()
    left, right = 0, len(nums) - 1
    while left <= right:
        l, r = abs(nums[left]), abs(nums[right])
        if l > r:
            squared_list.appendleft(l * l)
            l = +1
        else:
            squared_list.appendleft(r * r)
            r -= 1
    return list(squared_list)
