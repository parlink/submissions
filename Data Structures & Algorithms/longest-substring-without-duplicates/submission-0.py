class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        seen = defaultdict(int)

        for right in range(len(s)):
            seen[s[right]] += 1
            while seen[s[right]] > 1:
                seen[s[left]] -=1
                left +=1
            longest = max(longest, right - left + 1)
        return longest