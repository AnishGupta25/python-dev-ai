class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0: reurn
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1

        while j < len(nums):
            nums[j] = 0
            j += 1
        