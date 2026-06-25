import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix ,suffix , n = 1 , 1 , len(nums)
        max_prod = -math.inf
        for i in range(n):
            if prefix == 0: prefix = 1
            if suffix == 0: suffix = 1
            prefix *= nums[i]
            suffix *= nums[n-i-1]
            max_prod = max(max_prod,max(prefix, suffix))
        return max_prod