# INPUT: given a string with just the characters '(' & ')'
# OUTPUT: lenth of longest valid parantheses

# Time complexity is going to be o(N) + O(N) = O(2N) -> O(N)
# Space complexity is O(1) since no data structures are used
def longestVaidParentheses(s: str) -> int:
    left_count = right_count = max_count = 0
    i = 0

    while i < len(s):
        if s[i] == "(":
            left_count += 1
        else:
            right_count += 1

        if left_count == right_count:
            max_count = max(max_count, left_count + right_count)
        elif right_count > left_count:  # left:2, right:1 => (()
            left_count = right_count = 0

        i += 1

    left_count = right_count = 0
    i = len(s) - 1

    while i >= 0:
        if s[i] == "(":
            left_count += 1
        else:
            right_count += 1

        if left_count == right_count:
            max_count = max(max_count, left_count + right_count)
        elif left_count > right_count:
            left_count = right_count = 0

        i -= 1

    return max_count
