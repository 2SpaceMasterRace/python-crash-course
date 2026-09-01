    def containsDuplicate(nums: List[int]) -> bool:
        # input: array of integers = nums
        # Return True if values appear twice
        # Return False if every element is distinct 

        #Brute-Force - BigO(n^2)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        Return False

        #Sorting - BigO(nlogn)
        nums.sort()
        for i in range(1, len(nums)):
                # dupicates will be adjacent after sorting
                if nums[i] == nums[i-1]
                    return True
        return False

        # Hashset
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashet.add(n)
        Return False




