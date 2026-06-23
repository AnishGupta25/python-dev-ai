class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2: return nums
        pos , neg = 0 , 1
        ans = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                ans[pos] = nums[i]
                pos += 2
            else:
                ans[neg] = nums[i]
                neg += 2
        return ans