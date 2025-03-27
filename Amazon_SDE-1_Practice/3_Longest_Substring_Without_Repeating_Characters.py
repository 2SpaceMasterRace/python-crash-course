# INPUT: string s
# OUTPUT: length of longest substring without repeating characters

# Time complexity is O(N), where n is the length of the string
# Space complexity is O(N)


def lengthOfLongestSubstring(s: str) -> int:
    if len(s) <= 1:
        return len(s)

    position_dictionary = {}
    left_pointer = result = 0

    for right_pointer, char in enumerate(s):
        if char in position_dictionary:
            if position_dictionary[char] >= left_pointer:
                left_pointer = position_dictionary[char] + 1
        result = max(result, right_pointer - left_pointer + 1)

        position_dictionary[char] = right_pointer

    return result
