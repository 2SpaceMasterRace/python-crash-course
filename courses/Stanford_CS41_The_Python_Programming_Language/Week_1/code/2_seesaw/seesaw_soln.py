"""
File: seesaw.py
---------------
Write a function called seesaw_words, which takes in two strings and
prints out a pattern where the first word "turns into" the second word.
"""


def seesaw_words(s1, s2):
    # First, loop from the length of the string to 0...

    # The third parameter to range is the "step length", so here we are
    # stepping by -1, i.e., going in reverse. Alternatively, we could
    # loop for i in range(len(s1)) and then define k = len(s1) - i. As i
    # increases, k decreases.

    for i in range(len(s1), -1, -1):
        # Print the string, slicing it smaller and smaller
        print(s1[:i])

        # If the prefix is the same, stop printing s1
        if s1[:i] == s2[:i]:
            break

    # At this point, i is the last index and s[:i] was just printed
    # (that is, i still has the value it did at the end of the loop)
    for j in range(i + 1, len(s2) + 1):
        print(s2[:j])


if __name__ == '__main__':
    seesaw_words('telephone', 'television')
    seesaw_words('parth', 'tara')
    seesaw_words('telephone', 'megaphone')
