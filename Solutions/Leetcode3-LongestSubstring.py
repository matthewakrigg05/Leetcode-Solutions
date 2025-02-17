class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        longest = 0
        chars = set()
        left = 0

        for right in range(n):
            if s[right] not in chars:
                chars.add(s[right])
                longest = max(longest, right - left + 1)
            else:
                while s[right] in chars:
                    chars.remove(s[left])
                    left += 1
                chars.add(s[right])

        return longest
