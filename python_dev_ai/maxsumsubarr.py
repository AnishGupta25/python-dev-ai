import math
class Solution:
    def maxSubarraySum(self, arr):
        max = -math.inf
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
            if sum > max: max = sum
            if sum < 0: sum = 0
        return max