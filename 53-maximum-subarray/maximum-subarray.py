class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsub = nums[0]
        cur_sum = 0
        for i in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += i
            maxsub = max(maxsub, cur_sum)
        return maxsub 
        