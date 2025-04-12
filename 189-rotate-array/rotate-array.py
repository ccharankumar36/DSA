class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])



# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         for i in range(k):
#             a=nums.pop()
#             nums.insert(0,a)