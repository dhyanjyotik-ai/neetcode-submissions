class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count, count = 0, 0
        for e in nums:
            if e == 1:
                count += 1
                max_count = max(max_count, count)
                continue
            count = 0
        return max_count
        